package com.example.data

import androidx.room.Entity
import androidx.room.PrimaryKey

enum class TaskType {
    CHECKBOX, DURATION, COUNT, SPORTS, TRADING, QURAN, VIDEO, PRAYER
}

@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val title: String,
    val description: String? = null,
    val icon: String = "✅",
    val color: Long = 0xFF4CAF50, // Default green
    val type: TaskType = TaskType.CHECKBOX,
    val targetValue: Int = 1, // e.g. 45 for 45 mins, 5 for 5 pages
    val orderIndex: Int = 0,
    val isSystemTask: Boolean = false,
    val reminderTime: String? = null,
    val repeatDays: String = "1,2,3,4,5,6,7", // comma separated days of week
    val xpValue: Int = 10,
    val isWeeklyGoal: Boolean = false // New field for weekly goals
)

@Entity(tableName = "task_logs")
data class TaskLog(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val taskId: Int,
    val date: String, // YYYY-MM-DD format
    val completed: Boolean = false,
    val progress: Int = 0,
    val notes: String? = null,
    val extraData1: String? = null,
    val extraData2: String? = null,
    val extraData3: String? = null
)

@Entity(tableName = "user_stats")
data class UserStats(
    @PrimaryKey val id: Int = 1, // Singleton
    val level: Int = 1,
    val xp: Int = 0,
    val currentStreak: Int = 0,
    val longestStreak: Int = 0,
    val totalCompletedTasks: Int = 0
)
