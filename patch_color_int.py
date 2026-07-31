package com.example.data

import kotlinx.coroutines.flow.Flow
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class TaskRepository(private val taskDao: TaskDao) {
    val allTasks: Flow<List<Task>> = taskDao.getAllTasks()
    
    suspend fun hasTasks(): Boolean = taskDao.getTaskCount() > 0
    
    fun getLogsForDate(date: String): Flow<List<TaskLog>> {
        return taskDao.getTaskLogsForDate(date)
    }

    val userStats: Flow<UserStats?> = taskDao.getUserStats()

    suspend fun insertTask(task: Task) = taskDao.insertTask(task)
    suspend fun deleteTask(task: Task) = taskDao.deleteTask(task)
    
    suspend fun insertTaskLog(taskLog: TaskLog) = taskDao.insertTaskLog(taskLog)
    suspend fun updateTaskLog(taskLog: TaskLog) = taskDao.updateTaskLog(taskLog)
    
    suspend fun initializeDailyLogs(tasks: List<Task>, date: String) {
        tasks.forEach { task ->
            val existing = taskDao.getTaskLog(task.id, date)
            if (existing == null) {
                taskDao.insertTaskLog(TaskLog(taskId = task.id, date = date))
            }
        }
    }
    
    suspend fun updateUserStats(stats: UserStats) {
        val existing = taskDao.getUserStats()
        // Simple insert or update
        taskDao.insertUserStats(stats)
    }
    
    suspend fun toggleTaskCompletion(taskLog: TaskLog, isCompleted: Boolean) {
        taskDao.updateTaskLog(taskLog.copy(completed = isCompleted))
    }

    suspend fun populateDefaultTasks() {
        val defaultTasks = listOf(
            Task(title = "Sabah Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFF3B82F6, orderIndex = 0, isSystemTask = true),
            Task(title = "Öğle Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFF59E0B, orderIndex = 1, isSystemTask = true),
            Task(title = "İkindi Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFF97316, orderIndex = 2, isSystemTask = true),
            Task(title = "Akşam Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFEF4444, orderIndex = 3, isSystemTask = true),
            Task(title = "Yatsı Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFF8B5CF6, orderIndex = 4, isSystemTask = true),
            Task(title = "Kur'an Oku", type = TaskType.QURAN, icon = "📖", color = 0xFF10B981, orderIndex = 5, isSystemTask = true),
            Task(title = "Spor Yap", type = TaskType.SPORTS, icon = "🏋️", color = 0xFFF97316, orderIndex = 6, isSystemTask = true),
            Task(title = "Trading Backtesting", type = TaskType.TRADING, icon = "📈", color = 0xFF3B82F6, orderIndex = 7, isSystemTask = true),
            Task(title = "İslami İçerik İzle", type = TaskType.VIDEO, icon = "🎥", color = 0xFFEF4444, orderIndex = 8, isSystemTask = true)
        )
        defaultTasks.forEach { taskDao.insertTask(it) }
    }
}

fun getCurrentDateString(): String {
    val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
    return sdf.format(Date())
}
