"""
Tests for the TodoTask model of the application
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from todo.models import TodoTask


class TodoTaskModelTests(TestCase):

    def test_creating_todo_task_ok(self):
        """Tests creating a todo task works."""

        task_owner = get_user_model().objects.create_user(
            email="testuser@example.com",
            name="test user",
        )

        task_name = "Test Task"
        task_description = "A test task for our tests"

        task = TodoTask.objects.create(
            owner=task_owner,
            name=task_name,
            description=task_description,
        )

        self.assertEqual(task.owner, task_owner)
        self.assertEqual(task.name, task_name)
        self.assertEqual(task.description, task_description)
