"""
Excellent Code Practices - File 1/10
This file demonstrates exemplary Python coding standards and best practices.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Priority(Enum):
    """Enumeration for task priorities."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Task:
    """
    A well-documented task data class with type hints.
    
    Attributes:
        title: The task title
        description: Detailed task description
        priority: Task priority level
        completed: Whether the task is completed
        tags: Optional list of tags for categorization
    """
    title: str
    description: str
    priority: Priority
    completed: bool = False
    tags: Optional[List[str]] = None

    def __post_init__(self) -> None:
        """Initialize tags as empty list if None."""
        if self.tags is None:
            self.tags = []

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        logger.info(f"Task '{self.title}' marked as completed")

    def add_tag(self, tag: str) -> None:
        """
        Add a tag to the task.
        
        Args:
            tag: The tag to add
            
        Raises:
            ValueError: If tag is empty or already exists
        """
        if not tag.strip():
            raise ValueError("Tag cannot be empty")
        
        if tag in self.tags:
            raise ValueError(f"Tag '{tag}' already exists")
            
        self.tags.append(tag)


class TaskManager:
    """
    A comprehensive task management system with proper error handling,
    logging, and clean separation of concerns.
    """
    
    def __init__(self) -> None:
        """Initialize the task manager."""
        self._tasks: List[Task] = []
        logger.info("TaskManager initialized")

    def add_task(self, task: Task) -> None:
        """
        Add a task to the manager.
        
        Args:
            task: The task to add
            
        Raises:
            TypeError: If task is not a Task instance
        """
        if not isinstance(task, Task):
            raise TypeError("Expected Task instance")
            
        self._tasks.append(task)
        logger.info(f"Added task: {task.title}")

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """
        Get all tasks with the specified priority.
        
        Args:
            priority: The priority to filter by
            
        Returns:
            List of tasks with the specified priority
        """
        return [task for task in self._tasks if task.priority == priority]

    def get_completed_tasks(self) -> List[Task]:
        """
        Get all completed tasks.
        
        Returns:
            List of completed tasks
        """
        return [task for task in self._tasks if task.completed]

    def export_tasks_summary(self) -> Dict[str, Any]:
        """
        Export a comprehensive summary of all tasks.
        
        Returns:
            Dictionary containing task statistics and summaries
        """
        total_tasks = len(self._tasks)
        completed_tasks = len(self.get_completed_tasks())
        
        priority_breakdown = {
            priority.name: len(self.get_tasks_by_priority(priority))
            for priority in Priority
        }
        
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "completion_rate": completed_tasks / total_tasks if total_tasks > 0 else 0,
            "priority_breakdown": priority_breakdown,
            "pending_tasks": total_tasks - completed_tasks
        }


def create_sample_tasks() -> List[Task]:
    """
    Create sample tasks for demonstration purposes.
    
    Returns:
        List of sample tasks
    """
    return [
        Task(
            title="Implement user authentication",
            description="Add secure user login and registration functionality",
            priority=Priority.HIGH,
            tags=["security", "backend"]
        ),
        Task(
            title="Write unit tests",
            description="Comprehensive test coverage for core modules",
            priority=Priority.MEDIUM,
            tags=["testing", "quality"]
        ),
        Task(
            title="Update documentation",
            description="Refresh API documentation and user guides",
            priority=Priority.LOW,
            tags=["documentation"]
        )
    ]


def main() -> None:
    """
    Main function demonstrating excellent coding practices.
    """
    try:
        # Initialize task manager
        task_manager = TaskManager()
        
        # Add sample tasks
        sample_tasks = create_sample_tasks()
        for task in sample_tasks:
            task_manager.add_task(task)
        
        # Mark some tasks as completed
        sample_tasks[1].mark_completed()
        
        # Generate and display summary
        summary = task_manager.export_tasks_summary()
        logger.info(f"Task summary: {summary}")
        
        # Demonstrate priority filtering
        high_priority_tasks = task_manager.get_tasks_by_priority(Priority.HIGH)
        logger.info(f"High priority tasks: {len(high_priority_tasks)}")
        
    except Exception as error:
        logger.error(f"An error occurred: {error}")
        raise


if __name__ == "__main__":
    main()