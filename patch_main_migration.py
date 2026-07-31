package com.example.data

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Dao
interface ModuleDao {
    // Trading
    @Query("SELECT * FROM trading_sessions ORDER BY date DESC")
    fun getAllTradingSessions(): Flow<List<TradingSession>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTradingSession(session: TradingSession)

    // Workout
    @Query("SELECT * FROM workout_sessions ORDER BY date DESC")
    fun getAllWorkoutSessions(): Flow<List<WorkoutSession>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertWorkoutSession(session: WorkoutSession)

    // Quran
    @Query("SELECT * FROM quran_readings ORDER BY date DESC")
    fun getAllQuranReadings(): Flow<List<QuranReading>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertQuranReading(reading: QuranReading)

    // Planner
    @Query("SELECT * FROM planner_events ORDER BY time ASC")
    fun getAllPlannerEvents(): Flow<List<PlannerEvent>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertPlannerEvent(event: PlannerEvent)
    
    @Update
    suspend fun updatePlannerEvent(event: PlannerEvent)
    
    @Delete
    suspend fun deletePlannerEvent(event: PlannerEvent)

    // Achievements
    @Query("SELECT * FROM achievements")
    fun getAllAchievements(): Flow<List<Achievement>>
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAchievements(achievements: List<Achievement>)
    
    @Update
    suspend fun updateAchievement(achievement: Achievement)
}
