package com.example

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.data.*
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class ModuleViewModel(
    private val repository: ModuleRepository,
    private val taskRepository: TaskRepository
) : ViewModel() {

    val tradingSessions = repository.tradingSessions.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    val workoutSessions = repository.workoutSessions.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    val quranReadings = repository.quranReadings.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    val plannerEvents = repository.plannerEvents.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    val achievements = repository.achievements.stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    val userStats = taskRepository.userStats.stateIn(viewModelScope, SharingStarted.Lazily, UserStats())

    init {
        viewModelScope.launch {
            repository.achievements.collect { list ->
                if (list.isEmpty()) {
                    repository.insertAchievements(
                        listOf(
                            Achievement(title = "İlk Namaz Serisi", description = "7 gün namaz kıldın", icon = "🕌"),
                            Achievement(title = "7 Gün Disiplin", description = "7 gün boyunca hedeflerine ulaştın", icon = "🔥"),
                            Achievement(title = "30 Gün Disiplin", description = "30 gün boyunca hedeflerine ulaştın", icon = "🏆"),
                            Achievement(title = "İlk Hatim", description = "Kur'an'ı Kerim'i hatmettin", icon = "📖"),
                            Achievement(title = "100 Saat Backtesting", description = "100 saat trading backtesting yaptın", icon = "📈"),
                            Achievement(title = "100 Spor Antrenmanı", description = "100 kez spor yaptın", icon = "🏋️")
                        )
                    )
                }
            }
        }
    }

    fun addTradingSession(session: TradingSession) {
        viewModelScope.launch {
            repository.insertTradingSession(session)
            updateXP(150)
        }
    }

    fun addWorkoutSession(session: WorkoutSession) {
        viewModelScope.launch {
            repository.insertWorkoutSession(session)
            updateXP(150)
        }
    }

    fun addQuranReading(reading: QuranReading) {
        viewModelScope.launch {
            repository.insertQuranReading(reading)
            updateXP(120)
        }
    }
    
    fun addPlannerEvent(event: PlannerEvent) {
        viewModelScope.launch { repository.insertPlannerEvent(event) }
    }
    
    fun togglePlannerEvent(event: PlannerEvent, isCompleted: Boolean) {
        viewModelScope.launch { repository.updatePlannerEvent(event.copy(isCompleted = isCompleted)) }
    }
    
    fun deletePlannerEvent(event: PlannerEvent) {
        viewModelScope.launch { repository.deletePlannerEvent(event) }
    }

    private suspend fun updateXP(xpChange: Int) {
        val current = userStats.value
        val newXp = (current?.xp ?: 0) + xpChange
        val newLevel = (newXp / 100) + 1
        taskRepository.updateUserStats((current ?: UserStats()).copy(xp = newXp, level = newLevel))
    }
}
