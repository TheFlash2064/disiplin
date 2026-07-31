package com.example.data

import kotlinx.coroutines.flow.Flow

class ModuleRepository(private val moduleDao: ModuleDao) {
    val tradingSessions = moduleDao.getAllTradingSessions()
    val workoutSessions = moduleDao.getAllWorkoutSessions()
    val quranReadings = moduleDao.getAllQuranReadings()
    val plannerEvents = moduleDao.getAllPlannerEvents()
    val achievements = moduleDao.getAllAchievements()

    suspend fun insertTradingSession(session: TradingSession) = moduleDao.insertTradingSession(session)
    suspend fun insertWorkoutSession(session: WorkoutSession) = moduleDao.insertWorkoutSession(session)
    suspend fun insertQuranReading(reading: QuranReading) = moduleDao.insertQuranReading(reading)
    
    suspend fun insertPlannerEvent(event: PlannerEvent) = moduleDao.insertPlannerEvent(event)
    suspend fun updatePlannerEvent(event: PlannerEvent) = moduleDao.updatePlannerEvent(event)
    suspend fun deletePlannerEvent(event: PlannerEvent) = moduleDao.deletePlannerEvent(event)
    
    suspend fun insertAchievements(achievements: List<Achievement>) = moduleDao.insertAchievements(achievements)
    suspend fun updateAchievement(achievement: Achievement) = moduleDao.updateAchievement(achievement)
}
