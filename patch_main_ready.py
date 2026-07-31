package com.example

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.data.ModuleRepository
import com.example.data.TaskRepository

class ModuleViewModelFactory(
    private val moduleRepository: ModuleRepository,
    private val taskRepository: TaskRepository
) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(ModuleViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return ModuleViewModel(moduleRepository, taskRepository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
