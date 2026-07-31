package com.example.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.example.ModuleViewModel
import com.example.ui.theme.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PlannerScreen(viewModel: ModuleViewModel, navController: NavController) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Günlük Planlayıcı", color = MaterialTheme.colorScheme.onBackground) },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back", tint = MaterialTheme.colorScheme.onBackground)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = MaterialTheme.colorScheme.background)
            )
        },
        containerColor = MaterialTheme.colorScheme.background
    ) { padding ->
        Column(
            modifier = Modifier
                .padding(padding)
                .fillMaxSize()
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            val events by viewModel.plannerEvents.collectAsState()
            
            var showAddEvent by remember { mutableStateOf(false) }
            
            Button(
                onClick = { showAddEvent = true },
                modifier = Modifier.fillMaxWidth(),
                colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.primary)
            ) {
                Text("Yeni Plan Ekle")
            }
            
            LazyColumn(verticalArrangement = Arrangement.spacedBy(12.dp)) {
                items(events.sortedBy { it.time }) { event ->
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(12.dp))
                            .background(if (event.isCompleted) AccentGreen.copy(alpha = 0.2f) else MaterialTheme.colorScheme.surface)
                            .clickable { viewModel.togglePlannerEvent(event, !event.isCompleted) }
                            .padding(16.dp),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(event.time, fontSize = 14.sp, fontWeight = FontWeight.Bold, color = if (event.isCompleted) AccentGreen else MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.width(60.dp))
                            Text(event.title, fontSize = 16.sp, color = MaterialTheme.colorScheme.onBackground)
                        }
                        IconButton(onClick = { viewModel.deletePlannerEvent(event) }) {
                            Icon(androidx.compose.material.icons.Icons.Default.Delete, contentDescription = "Sil", tint = MaterialTheme.colorScheme.error)
                        }
                    }
                }
            }
            
            if (showAddEvent) {
                var newTime by remember { mutableStateOf("08:00") }
                var newTitle by remember { mutableStateOf("") }
                
                AlertDialog(
                    onDismissRequest = { showAddEvent = false },
                    title = { Text("Yeni Plan Ekle") },
                    text = {
                        Column {
                            OutlinedTextField(
                                value = newTime,
                                onValueChange = { newTime = it },
                                label = { Text("Saat (Örn: 08:00)") }
                            )
                            Spacer(modifier = Modifier.height(8.dp))
                            OutlinedTextField(
                                value = newTitle,
                                onValueChange = { newTitle = it },
                                label = { Text("Plan/Görev Adı") }
                            )
                        }
                    },
                    confirmButton = {
                        TextButton(onClick = {
                            if (newTime.isNotBlank() && newTitle.isNotBlank()) {
                                viewModel.addPlannerEvent(com.example.data.PlannerEvent(time = newTime, title = newTitle))
                                showAddEvent = false
                            }
                        }) {
                            Text("Ekle")
                        }
                    },
                    dismissButton = {
                        TextButton(onClick = { showAddEvent = false }) {
                            Text("İptal")
                        }
                    }
                )
            }
        }
    }
}
