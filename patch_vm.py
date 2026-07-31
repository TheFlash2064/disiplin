with open('app/src/main/java/com/example/TaskViewModel.kt', 'r') as f:
    content = f.read()

new_method = """
    fun saveTaskLog(taskLog: TaskLog) {
        viewModelScope.launch {
            repository.updateTaskLog(taskLog)
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
"""

content = content.replace("    fun addTask(task: Task) {", new_method + "    fun addTask(task: Task) {")

with open('app/src/main/java/com/example/TaskViewModel.kt', 'w') as f:
    f.write(content)
