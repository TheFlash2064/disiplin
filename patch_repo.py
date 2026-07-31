with open('app/src/main/java/com/example/data/TaskRepository.kt', 'r') as f:
    content = f.read()

old_tasks = """        val defaultTasks = listOf(
            Task(title = "Sabah Namazı", type = TaskType.CHECKBOX, icon = "🕌", color = 0xFF3B82F6, orderIndex = 0, isSystemTask = true),
            Task(title = "Öğle Namazı", type = TaskType.CHECKBOX, icon = "🕌", color = 0xFFF59E0B, orderIndex = 1, isSystemTask = true),
            Task(title = "İkindi Namazı", type = TaskType.CHECKBOX, icon = "🕌", color = 0xFFF97316, orderIndex = 2, isSystemTask = true),
            Task(title = "Akşam Namazı", type = TaskType.CHECKBOX, icon = "🕌", color = 0xFFEF4444, orderIndex = 3, isSystemTask = true),
            Task(title = "Yatsı Namazı", type = TaskType.CHECKBOX, icon = "🕌", color = 0xFF8B5CF6, orderIndex = 4, isSystemTask = true)
        )"""

new_tasks = """        val defaultTasks = listOf(
            Task(title = "Sabah Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFF3B82F6, orderIndex = 0, isSystemTask = true),
            Task(title = "Öğle Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFF59E0B, orderIndex = 1, isSystemTask = true),
            Task(title = "İkindi Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFF97316, orderIndex = 2, isSystemTask = true),
            Task(title = "Akşam Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFFEF4444, orderIndex = 3, isSystemTask = true),
            Task(title = "Yatsı Namazı", type = TaskType.PRAYER, icon = "🕌", color = 0xFF8B5CF6, orderIndex = 4, isSystemTask = true),
            Task(title = "Kur'an Oku", type = TaskType.QURAN, icon = "📖", color = 0xFF10B981, orderIndex = 5, isSystemTask = true),
            Task(title = "Spor Yap", type = TaskType.SPORTS, icon = "🏋️", color = 0xFFF97316, orderIndex = 6, isSystemTask = true),
            Task(title = "Trading Backtesting", type = TaskType.TRADING, icon = "📈", color = 0xFF3B82F6, orderIndex = 7, isSystemTask = true),
            Task(title = "İslami İçerik İzle", type = TaskType.VIDEO, icon = "🎥", color = 0xFFEF4444, orderIndex = 8, isSystemTask = true)
        )"""

content = content.replace(old_tasks, new_tasks)

with open('app/src/main/java/com/example/data/TaskRepository.kt', 'w') as f:
    f.write(content)
