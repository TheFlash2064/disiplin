with open('app/src/main/java/com/example/TaskViewModel.kt', 'r') as f:
    content = f.read()

content = content.replace(
"""    fun saveTaskLog(taskLog: TaskLog) {
        viewModelScope.launch {
            repository.updateTaskLog(taskLog)""",
"""    fun saveTaskLog(taskLog: TaskLog) {
        viewModelScope.launch {
            val existing = repository.getLogsForDate(currentDate.value).value?.find { it.taskId == taskLog.taskId }
            if (taskLog.id == 0 && existing == null) {
                repository.insertTaskLog(taskLog)
            } else if (taskLog.id == 0 && existing != null) {
                repository.updateTaskLog(taskLog.copy(id = existing.id))
            } else {
                repository.updateTaskLog(taskLog)
            }"""
)

with open('app/src/main/java/com/example/TaskViewModel.kt', 'w') as f:
    f.write(content)
