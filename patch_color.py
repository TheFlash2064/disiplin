package com.example.ui.screens

import androidx.compose.ui.platform.LocalContext
import com.example.NotificationHelper

import androidx.compose.animation.*
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.TaskViewModel
import com.example.TaskWithLog
import com.example.ui.theme.AccentOrange
import com.example.ui.theme.AccentGreen

import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.DateRange
import androidx.compose.material.icons.automirrored.filled.List
import androidx.compose.material.icons.automirrored.filled.MenuBook
import androidx.navigation.NavController
import com.example.data.Task
import com.example.ui.theme.AccentRed
import com.example.ui.theme.AccentBlue


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(viewModel: TaskViewModel, moduleViewModel: com.example.ModuleViewModel, navController: NavController) {
    val context = LocalContext.current
    val tasksWithLogs by viewModel.tasksWithLogs.collectAsStateWithLifecycle()
    val dailyTasks = remember(tasksWithLogs) { tasksWithLogs.filter { !it.task.isWeeklyGoal } }
    val weeklyGoals = remember(tasksWithLogs) { tasksWithLogs.filter { it.task.isWeeklyGoal } }
    val userStats by viewModel.userStats.collectAsStateWithLifecycle()

    var showAddTaskSheet by remember { mutableStateOf(false) }
    var taskToEdit by remember { mutableStateOf<Task?>(null) }
    var showTaskActionSheet by remember { mutableStateOf(false) }
    var activeTaskWithLog by remember { mutableStateOf<TaskWithLog?>(null) }

    val totalTasks = dailyTasks.size
    val completedTasks = dailyTasks.count { it.log?.completed == true }
    val progress = if (totalTasks > 0) (completedTasks.toFloat() / totalTasks.toFloat()) else 0f

    val animatedProgress by animateFloatAsState(
        targetValue = progress,
        animationSpec = tween(durationMillis = 1000, easing = FastOutSlowInEasing),
        label = "ProgressAnimation"
    )

    if (showTaskActionSheet && activeTaskWithLog != null) {
        TaskActionSheet(
            taskWithLog = activeTaskWithLog!!,
            onDismissRequest = { 
                showTaskActionSheet = false
                activeTaskWithLog = null
            },
            onSaveTaskLog = { newLog ->
                val finalLog = newLog.copy(date = viewModel.currentDate.value)
                viewModel.saveTaskLog(finalLog)
                val task = activeTaskWithLog?.task
                showTaskActionSheet = false
                activeTaskWithLog = null
                if (task != null) {
                    NotificationHelper.cancelNotification(context, task)
                }
            }
        )
    }
    
    if (showAddTaskSheet) {
        AddTaskSheet(
            taskToEdit = taskToEdit,
            onDismissRequest = {
                showAddTaskSheet = false
                taskToEdit = null
            },
            onSaveTask = { newTask ->
                if (taskToEdit != null) {
                    viewModel.updateTask(newTask)
                } else {
                    viewModel.addTask(newTask)
                }
                NotificationHelper.scheduleNotification(context, newTask)
                showAddTaskSheet = false
                taskToEdit = null
            }
        )
    }

    Scaffold(
        containerColor = MaterialTheme.colorScheme.background,
        contentWindowInsets = WindowInsets.safeDrawing,
        floatingActionButton = {
            FloatingActionButton(
                onClick = { showAddTaskSheet = true },
                containerColor = MaterialTheme.colorScheme.onBackground,
                contentColor = MaterialTheme.colorScheme.background,
                shape = CircleShape
            ) {
                Icon(Icons.Default.Add, contentDescription = "Add Task")
            }
        },
        floatingActionButtonPosition = FabPosition.Center,
        bottomBar = {
            NavigationBar(
                containerColor = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.9f),
                contentColor = MaterialTheme.colorScheme.onBackground,
                modifier = Modifier.clip(RoundedCornerShape(topStart = 24.dp, topEnd = 24.dp))
            ) {
                NavigationBarItem(
                    icon = { Icon(Icons.AutoMirrored.Filled.List, contentDescription = "Tasks") },
                    label = { Text("Görevler") },
                    selected = true,
                    onClick = { },
                    colors = NavigationBarItemDefaults.colors(
                        indicatorColor = MaterialTheme.colorScheme.onBackground,
                        selectedIconColor = MaterialTheme.colorScheme.background,
                        selectedTextColor = MaterialTheme.colorScheme.onBackground
                    )
                )
                NavigationBarItem(
                    icon = { Icon(Icons.AutoMirrored.Filled.MenuBook, contentDescription = "Dualar") },
                    label = { Text("Dualar") },
                    selected = false,
                    onClick = { navController.navigate("prophet_duas") },
                    colors = NavigationBarItemDefaults.colors(
                        indicatorColor = MaterialTheme.colorScheme.onBackground,
                        selectedIconColor = MaterialTheme.colorScheme.background,
                        selectedTextColor = MaterialTheme.colorScheme.onBackground
                    )
                )
                NavigationBarItem(
                    icon = { Icon(androidx.compose.material.icons.Icons.Default.DateRange, contentDescription = "Planlayıcı") },
                    label = { Text("Planlayıcı") },
                    selected = false,
                    onClick = { navController.navigate("planner") },
                    colors = NavigationBarItemDefaults.colors(
                        indicatorColor = MaterialTheme.colorScheme.onBackground,
                        selectedIconColor = MaterialTheme.colorScheme.background,
                        selectedTextColor = MaterialTheme.colorScheme.onBackground
                    )
                )
                NavigationBarItem(
                    icon = { Icon(androidx.compose.material.icons.Icons.Default.Person, contentDescription = "Profil") },
                    label = { Text("Profil") },
                    selected = false,
                    onClick = { navController.navigate("profile") },
                    colors = NavigationBarItemDefaults.colors(
                        indicatorColor = MaterialTheme.colorScheme.onBackground,
                        selectedIconColor = MaterialTheme.colorScheme.background,
                        selectedTextColor = MaterialTheme.colorScheme.onBackground
                    )
                )
            }
        }
    ) { padding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(horizontal = 24.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
            contentPadding = PaddingValues(bottom = 80.dp)
        ) {
            item {
                Column {
            Spacer(modifier = Modifier.height(16.dp))
            
            // Header: Top Profile
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                    Box(
                        modifier = Modifier
                            .size(40.dp)
                            .clip(CircleShape)
                            .background(MaterialTheme.colorScheme.surfaceVariant)
                            .border(1.dp, MaterialTheme.colorScheme.outlineVariant, CircleShape),
                        contentAlignment = Alignment.Center
                    ) {
                        Text("L${userStats.level}", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onBackground)
                    }
                    Column {
                        Text(
                            text = "DAILY LEVEL",
                            fontSize = 10.sp,
                            fontWeight = FontWeight.SemiBold,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            letterSpacing = 1.sp
                        )
                        Text(
                            text = "Muhammed Ali", // Could be dynamic
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Medium,
                            color = MaterialTheme.colorScheme.onBackground
                        )
                    }
                }
                
                // Streak Pill
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(50))
                        .background(MaterialTheme.colorScheme.surface)
                        .border(1.dp, MaterialTheme.colorScheme.outlineVariant, RoundedCornerShape(50))
                        .padding(horizontal = 12.dp, vertical = 6.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    Text("🔥", fontSize = 12.sp)
                    Text("${userStats.currentStreak} Days", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onBackground)
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Main Progress Circle & Quote
            Column(
                modifier = Modifier.fillMaxWidth(),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Box(
                    modifier = Modifier.size(140.dp),
                    contentAlignment = Alignment.Center
                ) {
                    val trackColor = MaterialTheme.colorScheme.surfaceVariant
                    val progressColor = MaterialTheme.colorScheme.onBackground
                    Canvas(modifier = Modifier.fillMaxSize()) {
                        drawArc(
                            color = trackColor,
                            startAngle = 0f,
                            sweepAngle = 360f,
                            useCenter = false,
                            style = Stroke(width = 6.dp.toPx(), cap = StrokeCap.Round)
                        )
                        drawArc(
                            color = progressColor,
                            startAngle = -90f,
                            sweepAngle = animatedProgress * 360f,
                            useCenter = false,
                            style = Stroke(width = 6.dp.toPx(), cap = StrokeCap.Round)
                        )
                    }
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Row(verticalAlignment = Alignment.Top) {
                            Text(
                                text = "${(animatedProgress * 100).toInt()}",
                                fontSize = 48.sp,
                                fontWeight = FontWeight.Light,
                                color = MaterialTheme.colorScheme.onBackground
                            )
                            Text(
                                text = "%",
                                fontSize = 24.sp,
                                color = MaterialTheme.colorScheme.onBackground.copy(alpha = 0.5f),
                                modifier = Modifier.padding(top = 8.dp)
                            )
                        }
                        Text(
                            text = "DISCIPLINE",
                            fontSize = 10.sp,
                            fontWeight = FontWeight.Medium,
                            letterSpacing = 2.sp,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                }
                
                Spacer(modifier = Modifier.height(16.dp))
                
                Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.padding(horizontal = 16.dp)) {
                    Text(
                        text = "“Verily, with hardship comes ease.”",
                        fontSize = 14.sp,
                        fontStyle = FontStyle.Italic,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        textAlign = TextAlign.Center
                    )
                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        text = "AL-INSHIRAH 94:6",
                        fontSize = 10.sp,
                        letterSpacing = 1.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.8f)
                    )
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

        }
    }

        // Task List
        if (weeklyGoals.isNotEmpty()) {
            item {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(top = 8.dp, bottom = 4.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text("HAFTALIK HEDEFLER", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, letterSpacing = 1.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
            }
            items(weeklyGoals, key = { it.task.id }) { taskWithLog ->
                TaskItem(
                    taskWithLog = taskWithLog,
                    onToggle = { isCompleted ->
                        viewModel.toggleTask(taskWithLog, isCompleted)
                        if (isCompleted) {
                            NotificationHelper.cancelNotification(context, taskWithLog.task)
                        } else {
                            NotificationHelper.scheduleNotification(context, taskWithLog.task)
                        }
                    },
                    onEdit = {
                        taskToEdit = taskWithLog.task
                        showAddTaskSheet = true
                    },
                    onDelete = {
                        viewModel.deleteTask(taskWithLog.task)
                        NotificationHelper.cancelNotification(context, taskWithLog.task)
                    }
                )
            }
            item { Spacer(modifier = Modifier.height(16.dp)) }
        }

        item {
            // Task List Header
            Row(
                modifier = Modifier.fillMaxWidth().padding(bottom = 8.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text("GÜNLÜK GÖREVLER", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, letterSpacing = 1.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                Text("$completedTasks / $totalTasks Tamamlandı", fontSize = 10.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        }

        items(dailyTasks, key = { it.task.id }) { taskWithLog ->
            TaskItem(
                taskWithLog = taskWithLog,
                onToggle = { isCompleted ->
                    viewModel.toggleTask(taskWithLog, isCompleted)
                    if (isCompleted) {
                        NotificationHelper.cancelNotification(context, taskWithLog.task)
                    } else {
                        NotificationHelper.scheduleNotification(context, taskWithLog.task)
                    }
                },
                onEdit = {
                    taskToEdit = taskWithLog.task
                    showAddTaskSheet = true
                },
                onDelete = {
                    viewModel.deleteTask(taskWithLog.task)
                    NotificationHelper.cancelNotification(context, taskWithLog.task)
                }
            )
        }
    }
}

}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TaskItem(
    taskWithLog: TaskWithLog,
    onToggle: (Boolean) -> Unit,
    onClick: () -> Unit = { onToggle(!(taskWithLog.log?.completed == true)) },
    onEdit: () -> Unit = {},
    onDelete: () -> Unit = {}
) {
    val isCompleted = taskWithLog.log?.completed == true
    val task = taskWithLog.task

    val dismissState = rememberSwipeToDismissBoxState(
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
        enableDismissFromEndToStart = !task.isSystemTask,
        backgroundContent = {
            val direction = dismissState.dismissDirection
            val alignment = when (direction) {
                SwipeToDismissBoxValue.StartToEnd -> Alignment.CenterStart
                SwipeToDismissBoxValue.EndToStart -> Alignment.CenterEnd
                else -> Alignment.Center
            }
            val color = when (direction) {
                SwipeToDismissBoxValue.StartToEnd -> AccentBlue.copy(alpha = 0.8f)
                SwipeToDismissBoxValue.EndToStart -> AccentRed.copy(alpha = 0.8f)
                else -> Color.Transparent
            }
            val icon = when (direction) {
                SwipeToDismissBoxValue.StartToEnd -> Icons.Default.Edit
                SwipeToDismissBoxValue.EndToStart -> Icons.Default.Delete
                else -> null
            }

            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(vertical = 4.dp)
                    .clip(RoundedCornerShape(16.dp))
                    .background(color)
                    .padding(horizontal = 24.dp),
                contentAlignment = alignment
            ) {
                if (icon != null) {
                    Icon(icon, contentDescription = null, tint = Color.White)
                }
            }
        }
    ) {
        val backgroundColor by animateColorAsState(
            targetValue = if (isCompleted) MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f) else MaterialTheme.colorScheme.surface,
            animationSpec = tween(300),
            label = "backgroundColor"
        )

        val checkboxColor by animateColorAsState(
            targetValue = if (isCompleted) AccentGreen.copy(alpha = 0.2f) else Color.Transparent,
            animationSpec = tween(300),
            label = "checkboxColor"
        )

        val borderColor by animateColorAsState(
            targetValue = if (isCompleted) AccentGreen else MaterialTheme.colorScheme.surfaceVariant,
            animationSpec = tween(300),
            label = "borderColor"
        )
        
        val textAlpha by animateFloatAsState(
            targetValue = if (isCompleted) 0.5f else 1f,
            animationSpec = tween(300),
            label = "textAlpha"
        )

        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 4.dp)
                .clip(RoundedCornerShape(16.dp))
                .background(backgroundColor)
                .border(1.dp, MaterialTheme.colorScheme.outlineVariant, RoundedCornerShape(16.dp))
                .clickable { onClick() }
                .padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Icon Box
            Box(
                modifier = Modifier
                    .size(40.dp)
                    .clip(RoundedCornerShape(12.dp))
                    .background(Color(task.color.toInt()).copy(alpha = 0.1f)),
                contentAlignment = Alignment.Center
            ) {
                Text(text = task.icon, fontSize = 20.sp)
            }

            Spacer(modifier = Modifier.width(16.dp))

            // Titles
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = task.title,
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Medium,
                    color = MaterialTheme.colorScheme.onBackground.copy(alpha = textAlpha)
                )
                if (!task.description.isNullOrEmpty()) {
                    Text(
                        text = task.description,
                        fontSize = 10.sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = textAlpha)
                    )
                }
            }

            Spacer(modifier = Modifier.width(16.dp))

            // Circular Checkbox
            Box(
                modifier = Modifier
                    .size(32.dp)
                    .clip(CircleShape)
                    .background(checkboxColor)
                    .border(2.dp, borderColor, CircleShape),
                contentAlignment = Alignment.Center
            ) {
                val checkScale by animateFloatAsState(
                    targetValue = if (isCompleted) 1f else 0f,
                    animationSpec = tween(300),
                    label = "checkScale"
                )
                if (checkScale > 0.01f) {
                    Icon(
                        imageVector = Icons.Default.Check,
                        contentDescription = "Tamamlandı",
                        tint = AccentGreen,
                        modifier = Modifier.size((16 * checkScale).dp)
                    )
                }
            }
        }
    }
}

@Composable
fun ModuleCard(
    title: String,
    icon: String,
    color: Color,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .clip(RoundedCornerShape(16.dp))
            .background(MaterialTheme.colorScheme.surface)
            .border(1.dp, MaterialTheme.colorScheme.outlineVariant, RoundedCornerShape(16.dp))
            .clickable(onClick = onClick)
            .padding(vertical = 16.dp, horizontal = 8.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Box(
            modifier = Modifier
                .size(40.dp)
                .clip(CircleShape)
                .background(color.copy(alpha = 0.2f)),
            contentAlignment = Alignment.Center
        ) {
            Text(icon, fontSize = 20.sp)
        }
        Spacer(modifier = Modifier.height(8.dp))
        Text(title, fontSize = 12.sp, fontWeight = FontWeight.Medium, color = MaterialTheme.colorScheme.onBackground)
    }
}
