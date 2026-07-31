with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'r') as f:
    content = f.read()

target = """    val dismissState = rememberSwipeToDismissBoxState(
        confirmValueChange = { dismissValue ->
            if (task.isSystemTask) return@rememberSwipeToDismissBoxState false

            when (dismissValue) {
                SwipeToDismissBoxValue.StartToEnd -> {
                    onEdit()
                    false // Don't actually dismiss, just trigger edit
                }
                SwipeToDismissBoxValue.EndToStart -> {
                    onDelete()
                    true // Dismiss and delete
                }
                else -> false
            }
        }
    )

    SwipeToDismissBox(
        state = dismissState,
        enableDismissFromStartToEnd = !task.isSystemTask,
        enableDismissFromEndToStart = !task.isSystemTask,"""

replacement = """    val dismissState = rememberSwipeToDismissBoxState(
        confirmValueChange = { dismissValue ->
            when (dismissValue) {
                SwipeToDismissBoxValue.StartToEnd -> {
                    onEdit()
                    false // Don't actually dismiss, just trigger edit
                }
                SwipeToDismissBoxValue.EndToStart -> {
                    if (task.isSystemTask) return@rememberSwipeToDismissBoxState false
                    onDelete()
                    true // Dismiss and delete
                }
                else -> false
            }
        }
    )

    SwipeToDismissBox(
        state = dismissState,
        enableDismissFromStartToEnd = true,
        enableDismissFromEndToStart = !task.isSystemTask,"""

content = content.replace(target, replacement)

target2 = """    val dismissState = rememberSwipeToDismissBoxState(
        confirmValueChange = { dismissValue ->
            if (task.isSystemTask) return@rememberSwipeToDismissBoxState false
            when (dismissValue) {
                SwipeToDismissBoxValue.StartToEnd -> {
                    onEdit()
                    false // Don't actually dismiss, just trigger edit
                }
                SwipeToDismissBoxValue.EndToStart -> {
                    onDelete()
                    true // Dismiss and delete
                }
                else -> false
            }
        }
    )

    SwipeToDismissBox(
        state = dismissState,
        enableDismissFromStartToEnd = !task.isSystemTask,
        enableDismissFromEndToStart = !task.isSystemTask,"""

content = content.replace(target2, replacement)

with open('app/src/main/java/com/example/ui/screens/HomeScreen.kt', 'w') as f:
    f.write(content)
