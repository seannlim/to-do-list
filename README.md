# Sean's To-Do List

This is a simple command-line to-do list application that allows you to add, remove, and list tasks. The tasks are saved in a CSV file and can be loaded the next time you run the program.

## Features

- **Add Task**: Add a task with a description, priority (high, medium, low), and due date (YYYY-MM-DD format).
- **Remove Task**: Remove a task by its description.
- **List Tasks**: Displays the current list of tasks in a tabular format.
- **Save and Load Tasks**: Tasks are automatically saved to a CSV file when the program exits and loaded when the program starts.

## Requirements

- Python 3.x
- `tabulate` library (for pretty-printing the tasks)

You can install the `tabulate` library using pip:

```bash
pip install tabulate
```

## How to Use

**1. Clone the Repository**: Download the code to your local machine.
**2. Run the Program**: Use the following command to start the program:
```bash
python to_do_list.py
```
**3. Main Menu Option**:
- Add Task: Enter the task description, priority (high, medium, low), and due date (YYYY-MM-DD format). The task will be added if the due date is valid and in the future.
- Remove Task: Enter the description of the task you want to remove.
- List Tasks: View all current tasks in a formatted table.
- Exit: Save all tasks to tasks.csv and exit the program.
   
## CSV File Format
Tasks are saved in a tasks.csv file with the following columns:

- **description**: The task description.
- **priority**: The task priority (high, medium, low).
- **due_date**: The due date of the task in **YYYY-MM-DD** format.

## Example
```bash
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
```

## Notes 
- The program validates the due date to ensure it is not in the past.
- If the tasks.csv file does not exist, it will be created when you add tasks and exit the program.
- The program does not allow duplicate descriptions for tasks.
