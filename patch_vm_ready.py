with open('app/src/main/java/com/example/TaskViewModel.kt', 'r') as f:
    content = f.read()

ready_state = """    private val _isReady = MutableStateFlow(false)
    val isReady: StateFlow<Boolean> = _isReady.asStateFlow()
"""

content = content.replace("    private val _currentDate = MutableStateFlow(getCurrentDateString())", ready_state + "    private val _currentDate = MutableStateFlow(getCurrentDateString())")

init_start = """    init {
        viewModelScope.launch {
            if (!repository.hasTasks()) {
                repository.populateDefaultTasks()
            }"""

init_replacement = """    init {
        viewModelScope.launch {
            if (!repository.hasTasks()) {
                repository.populateDefaultTasks()
            }
            _isReady.value = true"""

content = content.replace(init_start, init_replacement)

with open('app/src/main/java/com/example/TaskViewModel.kt', 'w') as f:
    f.write(content)
