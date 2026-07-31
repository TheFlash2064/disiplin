package com.example

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.data.*
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch

data class TaskWithLog(
    val task: Task,
    val log: TaskLog?
)

class TaskViewModel(private val repository: TaskRepository) : ViewModel() {

    private val _isReady = MutableStateFlow(false)
    val isReady: StateFlow<Boolean> = _isReady.asStateFlow()
    private val _currentDate = MutableStateFlow(getCurrentDateString())
    val currentDate: StateFlow<String> = _currentDate.asStateFlow()

    val tasks = repository.allTasks.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    
    @OptIn(kotlinx.coroutines.ExperimentalCoroutinesApi::class)
    val dailyLogs: StateFlow<List<TaskLog>> = _currentDate
        .flatMapLatest { date -> repository.getLogsForDate(date) }
        .stateIn(viewModelScope, SharingStarted.Lazily, emptyList())

    val tasksWithLogs: StateFlow<List<TaskWithLog>> = combine(tasks, dailyLogs) { ts, logs ->
        ts.map { t -> 
            TaskWithLog(task = t, log = logs.find { it.taskId == t.id })
        }
    }.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())

    val userStats: StateFlow<UserStats> = repository.userStats
        .map { it ?: UserStats() }
        .stateIn(viewModelScope, SharingStarted.Lazily, UserStats())

    init {
        viewModelScope.launch {
            if (!repository.hasTasks()) {
                repository.populateDefaultTasks()
            }
            _isReady.value = true
        }
        
        // Initialize logs for today if they don't exist
        viewModelScope.launch {
            tasks.collectLatest { currentTasks ->
                if (currentTasks.isNotEmpty()) {
                    repository.initializeDailyLogs(currentTasks, _currentDate.value)
                }
            }
        }
    }

    fun toggleTask(taskWithLog: TaskWithLog, isCompleted: Boolean) {
        viewModelScope.launch {
            if (taskWithLog.log != null) {
                repository.toggleTaskCompletion(taskWithLog.log, isCompleted)
            } else {
                val newLog = TaskLog(taskId = taskWithLog.task.id, date = _currentDate.value, completed = isCompleted)
                repository.insertTaskLog(newLog)
            }
            updateXP(if (isCompleted) 10 else -10)
            if (isCompleted) updateStreak()
        }
    }


    fun saveTaskLog(taskLog: TaskLog) {
        viewModelScope.launch {
            val existingLog = dailyLogs.value.find { it.taskId == taskLog.taskId }
            if (taskLog.id == 0 && existingLog != null) {
                repository.updateTaskLog(taskLog.copy(id = existingLog.id))
            } else if (taskLog.id == 0) {
                repository.insertTaskLog(taskLog)
            } else {
                repository.updateTaskLog(taskLog)
            }
            if (taskLog.completed) {
                updateXP(10) // XP for completing a detailed task
                updateStreak()
            }
        }
    }

    private suspend fun updateStreak() {
        val current = userStats.value
        val newStreak = current.currentStreak + 1
        val longest = maxOf(newStreak, current.longestStreak)
        repository.updateUserStats(current.copy(currentStreak = newStreak, longestStreak = longest, totalCompletedTasks = current.totalCompletedTasks + 1))
    }
    fun addTask(task: Task) {
        viewModelScope.launch {
            repository.insertTask(task)
        }
    }

    fun updateTask(task: Task) {
        viewModelScope.launch {
            repository.insertTask(task) // insert with replace
        }
    }

    fun deleteTask(task: Task) {
        viewModelScope.launch {
            if (!task.isSystemTask) {
                repository.deleteTask(task)
            }
        }
    }

    private suspend fun updateXP(xpChange: Int) {
        val current = userStats.value
        val newXp = (current.xp + xpChange).coerceAtLeast(0)
        val newLevel = (newXp / 100) + 1
        repository.updateUserStats(current.copy(xp = newXp, level = newLevel))
    }
}
