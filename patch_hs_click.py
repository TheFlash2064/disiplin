package com.example.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.data.Task
import com.example.data.TaskType

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddTaskSheet(
    taskToEdit: Task? = null,
    onDismissRequest: () -> Unit,
    onSaveTask: (Task) -> Unit
) {
    var title by remember { mutableStateOf(taskToEdit?.title ?: "") }
    var description by remember { mutableStateOf(taskToEdit?.description ?: "") }
    var icon by remember { mutableStateOf(taskToEdit?.icon ?: "✅") }
    var reminderTime by remember { mutableStateOf(taskToEdit?.reminderTime ?: "") }

    ModalBottomSheet(
        onDismissRequest = onDismissRequest,
        containerColor = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            Text(
                text = if (taskToEdit != null) "Görevi Düzenle" else "Yeni Görev Ekle",
                style = MaterialTheme.typography.titleLarge,
                color = MaterialTheme.colorScheme.onBackground
            )

            Spacer(modifier = Modifier.height(16.dp))

            OutlinedTextField(
                value = title,
                onValueChange = { title = it },
                label = { Text("Görev Adı") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true
            )

            Spacer(modifier = Modifier.height(8.dp))

            OutlinedTextField(
                value = description,
                onValueChange = { description = it },
                label = { Text("Açıklama (İsteğe bağlı)") },
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(8.dp))
            
            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                OutlinedTextField(
                    value = icon,
                    onValueChange = { icon = it },
                    label = { Text("Emoji") },
                    modifier = Modifier.weight(1f),
                    singleLine = true
                )
                OutlinedTextField(
                    value = reminderTime,
                    onValueChange = { reminderTime = it },
                    label = { Text("Saat (örn: 22:00)") },
                    modifier = Modifier.weight(1f),
                    singleLine = true
                )
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            var isWeeklyGoal by remember { mutableStateOf(taskToEdit?.isWeeklyGoal == true) }
            var isSaving by remember { mutableStateOf(false) }
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = androidx.compose.ui.Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Text("Haftalık Hedef mi?", color = MaterialTheme.colorScheme.onBackground)
                Switch(checked = isWeeklyGoal, onCheckedChange = { isWeeklyGoal = it })
            }

            Spacer(modifier = Modifier.height(24.dp))

            Button(
                onClick = {
                    if (title.isNotBlank() && !isSaving) {
                        isSaving = true
                        val newTask = taskToEdit?.copy(
                            title = title,
                            description = description,
                            icon = icon,
                            reminderTime = reminderTime,
                            isWeeklyGoal = isWeeklyGoal
                        ) ?: Task(
                            title = title,
                            description = description.ifBlank { null },
                            icon = icon.ifBlank { "✅" },
                            reminderTime = reminderTime.ifBlank { null },
                            type = TaskType.CHECKBOX,
                            isWeeklyGoal = isWeeklyGoal
                        )
                        onSaveTask(newTask)
                    }
                },
                modifier = Modifier.fillMaxWidth(),
                colors = ButtonDefaults.buttonColors(
                    containerColor = MaterialTheme.colorScheme.onBackground,
                    contentColor = MaterialTheme.colorScheme.background
                ),
                shape = RoundedCornerShape(12.dp)
            ) {
                Text("Kaydet")
            }
            
            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
