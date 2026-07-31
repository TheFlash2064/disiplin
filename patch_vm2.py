with open('app/src/main/java/com/example/TaskViewModel.kt', 'r') as f:
    content = f.read()

content = content.replace("updateXP(if (isCompleted) 10 else -10)", "updateXP(if (isCompleted) 10 else -10)\n            if (isCompleted) updateStreak()")

with open('app/src/main/java/com/example/TaskViewModel.kt', 'w') as f:
    f.write(content)
