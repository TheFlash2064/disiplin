package com.example.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "trading_sessions")
data class TradingSession(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val date: String,
    val durationMinutes: Int,
    val tradesAnalyzed: Int,
    val setupsFound: Int,
    val winRate: Float,
    val riskReward: Float,
    val notes: String
)

@Entity(tableName = "workout_sessions")
data class WorkoutSession(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val date: String,
    val durationMinutes: Int,
    val muscleGroup: String,
    val heightCm: Float,
    val weightKg: Float,
    val bodyMeasurements: String // JSON or simple string
)

@Entity(tableName = "quran_readings")
data class QuranReading(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val date: String,
    val pagesRead: Int,
    val surahName: String
)

@Entity(tableName = "planner_events")
data class PlannerEvent(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val time: String, // e.g. "08:00"
    val title: String,
    val isCompleted: Boolean = false
)

@Entity(tableName = "achievements")
data class Achievement(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val title: String,
    val description: String,
    val isUnlocked: Boolean = false,
    val icon: String
)
