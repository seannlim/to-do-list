import pytest
import os
from datetime import datetime
from project import add_task, remove_task, list_tasks, save_tasks, load_tasks

# Sample data for testing
test_tasks = [
    {"description": "Buy groceries", "priority": "high", "due_date": "2024-10-01"},
    {"description": "Read a book", "priority": "medium", "due_date": "2024-10-10"}
]

def test_add_task():
    tasks = []
    result = add_task(tasks, "Test task", "low", "2024-10-30")
    assert result == True
    assert len(tasks) == 1
    assert tasks[0] == {"description": "Test task", "priority": "low", "due_date": "2024-10-30"}

def test_add_task_invalid_date():
    tasks = []
    result = add_task(tasks, "Test task", "low", "2023-10-30")
    assert result == False
    assert len(tasks) == 0

def test_remove_task():
    tasks = test_tasks.copy()
    tasks = remove_task(tasks, "Read a book")
    assert len(tasks) == 1
    assert tasks[0] == {"description": "Buy groceries", "priority": "high", "due_date": "2024-10-01"}

def test_save_and_load_tasks():
    # Save tasks to a file
    save_tasks(test_tasks)
    assert os.path.exists("tasks.csv")

    # Load tasks from the file
    loaded_tasks = load_tasks()
    assert len(loaded_tasks) == len(test_tasks)
    assert loaded_tasks[0] == test_tasks[0]
    assert loaded_tasks[1] == test_tasks[1]

# Cleanup the test CSV file after tests
@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    if os.path.exists("tasks.csv"):
        os.remove("tasks.csv")
