# Sean's To-Do List Program

This is a simple command-line based to-do list program written in Python. The program allows users to add, remove, and list tasks with associated priorities and due dates. Tasks are saved to and loaded from a CSV file, making it easy to manage tasks between sessions.

## Features

- **Add Task**: Allows the user to add a new task with a description, priority, and due date.
- **Remove Task**: Enables the user to remove a task by its description.
- **List Tasks**: Displays the current list of tasks in a tabular format.
- **Save and Load Tasks**: Tasks are automatically saved to a CSV file when the program exits and loaded when the program starts.

## Requirements

- Python 3.x
- `tabulate` library (for pretty-printing the tasks)

You can install the `tabulate` library using pip:

```bash
pip install tabulate

How to Use
Clone the Repository: Download the code to your local machine.

Run the Program: Use the following command to start the program:

bash
Copy code
python to_do_list.py
Main Menu Options:

1. Add Task: Enter the task description, priority (high, medium, low), and due date (YYYY-MM-DD format). The task will be added if the due date is valid and in the future.

2. Remove Task: Enter the description of the task you want to remove.

3. List Tasks: View all current tasks in a formatted table.

4. Exit: Save all tasks to tasks.csv and exit the program.

CSV File Format
The tasks are saved in a tasks.csv file with the following columns:

description: The task description.
priority: The task priority (high, medium, low).
due_date: The due date of the task in YYYY-MM-DD format.
Example
plaintext
Copy code
Sean's To-Do List Menu:
1. Add Task
2. Remove Task
3. List Tasks
4. Exit
Enter your choice: 1
Enter task description: Finish project
Enter priority (high, medium, low): high
Enter due date (YYYY-MM-DD): 2024-08-30
Task added successfully.

Sean's To-Do List Menu:
1. Add Task
2. Remove Task
3. List Tasks
4. Exit
Enter your choice: 3

Sean's Current To-Do List:
+------------------+----------+------------+
| description      | priority | due_date   |
+------------------+----------+------------+
| Finish project   | high     | 2024-08-30 |
+------------------+----------+------------+
Notes
The program validates the due date to ensure it is not in the past.
If the tasks.csv file does not exist, it will be created when you add tasks and exit the program.
The program does not allow duplicate descriptions for tasks.
License
This project is open-source and available under the MIT License.
