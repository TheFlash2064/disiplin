package com.example.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.data.TaskLog
import com.example.data.TaskType
import com.example.TaskWithLog

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TaskActionSheet(
    taskWithLog: TaskWithLog,
    onDismissRequest: () -> Unit,
    onSaveTaskLog: (TaskLog) -> Unit
) {
    val task = taskWithLog.task
    val log = taskWithLog.log
    
    var extraData1 by remember { mutableStateOf(log?.extraData1 ?: "") }
    var extraData2 by remember { mutableStateOf(log?.extraData2 ?: "") }
    var extraData3 by remember { mutableStateOf(log?.extraData3 ?: "") }
    var notes by remember { mutableStateOf(log?.notes ?: "") }
    
    var isSaving by remember { mutableStateOf(false) }

    ModalBottomSheet(
        onDismissRequest = onDismissRequest,
        containerColor = MaterialTheme.colorScheme.background
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 24.dp, vertical = 16.dp)
        ) {
            Text(
                text = "${task.icon} ${task.title}",
                style = MaterialTheme.typography.titleLarge,
                color = MaterialTheme.colorScheme.onBackground
            )
            Spacer(modifier = Modifier.height(16.dp))

            when (task.type) {
                TaskType.SPORTS -> {
                    OutlinedTextField(
                        value = extraData1,
                        onValueChange = { extraData1 = it },
                        label = { Text("Antrenman Türü") },
                        modifier = Modifier.fillMaxWidth()
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    OutlinedTextField(
                        value = extraData2,
                        onValueChange = { extraData2 = it },
                        label = { Text("Süre (dk)") },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
                TaskType.TRADING -> {
                    OutlinedTextField(
                        value = extraData1,
                        onValueChange = { extraData1 = it },
                        label = { Text("Kaç işlem incelendi") },
                        modifier = Modifier.fillMaxWidth()
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    OutlinedTextField(
                        value = extraData2,
                        onValueChange = { extraData2 = it },
                        label = { Text("Backtesting Süresi (dk)") },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
                TaskType.QURAN -> {
                    OutlinedTextField(
                        value = extraData1,
                        onValueChange = { extraData1 = it },
                        label = { Text("Kaç sayfa okundu") },
                        modifier = Modifier.fillMaxWidth()
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    OutlinedTextField(
                        value = extraData2,
                        onValueChange = { extraData2 = it },
                        label = { Text("Hangi sure (İsteğe bağlı)") },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
                TaskType.VIDEO -> {
                    OutlinedTextField(
                        value = extraData1,
                        onValueChange = { extraData1 = it },
                        label = { Text("Bugün ne izlendi") },
                        modifier = Modifier.fillMaxWidth()
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    OutlinedTextField(
                        value = extraData2,
                        onValueChange = { extraData2 = it },
                        label = { Text("Süre (dk)") },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
                TaskType.PRAYER -> {
                    Row(verticalAlignment = androidx.compose.ui.Alignment.CenterVertically) {
                        Checkbox(
                            checked = extraData1 == "Cemaatle",
                            onCheckedChange = { extraData1 = if (it) "Cemaatle" else "" }
                        )
                        Text("Cemaatle kıldım", color = MaterialTheme.colorScheme.onBackground)
                    }
                }
                else -> {
                    // Standard task, maybe just notes
                }
            }
            
            if (task.type != TaskType.PRAYER) {
                Spacer(modifier = Modifier.height(8.dp))
                OutlinedTextField(
                    value = notes,
                    onValueChange = { notes = it },
                    label = { Text("Not") },
                    modifier = Modifier.fillMaxWidth()
                )
            }

            Spacer(modifier = Modifier.height(24.dp))
            Button(
                onClick = {
                    if (!isSaving) {
                        isSaving = true
                        val newLog = log?.copy(
                            completed = true,
                            notes = notes.ifBlank { null },
                            extraData1 = extraData1.ifBlank { null },
                            extraData2 = extraData2.ifBlank { null },
                            extraData3 = extraData3.ifBlank { null }
                        ) ?: TaskLog(
                            taskId = task.id,
                            date = "", // We'll set this in the ViewModel
                            completed = true,
                            notes = notes.ifBlank { null },
                            extraData1 = extraData1.ifBlank { null },
                            extraData2 = extraData2.ifBlank { null },
                            extraData3 = extraData3.ifBlank { null }
                        )
                        onSaveTaskLog(newLog)
                    }
                },
                modifier = Modifier.fillMaxWidth(),
                colors = ButtonDefaults.buttonColors(
                    containerColor = MaterialTheme.colorScheme.onBackground,
                    contentColor = MaterialTheme.colorScheme.background
                ),
                shape = RoundedCornerShape(12.dp)
            ) {
                Text(if (log?.completed == true) "Güncelle" else "Tamamla")
            }
            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}
