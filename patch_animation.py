package com.example.data

import androidx.room.*
import kotlinx.coroutines.flow.Flow

@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks ORDER BY orderIndex ASC")
    fun getAllTasks(): Flow<List<Task>>

    @Query("SELECT COUNT(*) FROM tasks")
    suspend fun getTaskCount(): Int

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTask(task: Task): Long

    @Delete
    suspend fun deleteTask(task: Task)

    // TaskLogs
    @Query("SELECT * FROM task_logs WHERE date = :date")
    fun getTaskLogsForDate(date: String): Flow<List<TaskLog>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTaskLog(taskLog: TaskLog)
    
    @Update
    suspend fun updateTaskLog(taskLog: TaskLog)

    @Query("SELECT * FROM task_logs WHERE taskId = :taskId AND date = :date LIMIT 1")
    suspend fun getTaskLog(taskId: Int, date: String): TaskLog?

    // Stats
    @Query("SELECT * FROM user_stats WHERE id = 1")
    fun getUserStats(): Flow<UserStats?>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUserStats(stats: UserStats)

    @Update
    suspend fun updateUserStats(stats: UserStats)
}

@Database(
    entities = [
        Task::class, 
        TaskLog::class, 
        UserStats::class,
        TradingSession::class,
        WorkoutSession::class,
        QuranReading::class,
        PlannerEvent::class,
        Achievement::class
    ], 
    version = 4, 
    exportSchema = false
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun taskDao(): TaskDao
    abstract fun moduleDao(): ModuleDao
}
