with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'r') as f:
    content = f.read()

content = content.replace(
"""fun TaskItem(
    taskWithLog: TaskWithLog,
    onToggle: (Boolean) -> Unit,
    onEdit: () -> Unit = {},
    onDelete: () -> Unit = {}
)""",
"""fun TaskItem(
    taskWithLog: TaskWithLog,
    onToggle: (Boolean) -> Unit,
    onClick: () -> Unit = { onToggle(!(taskWithLog.log?.completed == true)) },
    onEdit: () -> Unit = {},
    onDelete: () -> Unit = {}
)"""
)

content = content.replace(
"                .clickable { onToggle(!isCompleted) }",
"                .clickable { onClick() }"
)

with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'w') as f:
    f.write(content)
