import csv
from datetime import datetime
from tabulate import tabulate

# Main function that runs the to-do list program
def main():
    tasks = load_tasks()

    while True:
        print("\nSean's To-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if add_task(tasks, description, priority, due_date):
                print("Task added successfully.")
            else:
                print("Invalid due date. Task not added.")
        elif choice == '2':
            description = input("Enter task description to remove: ")
            tasks = remove_task(tasks, description)
        elif choice == '3':
            current_tasks = list_tasks(tasks)
            print("\nSean's Current To-Do List:")
            # Convert tasks to table format and print
            print(tabulate(current_tasks, headers="keys", tablefmt="grid"))
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a task to the tasks list
def add_task(tasks, description, priority, due_date):
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        if due_date_obj < datetime.now():
            return False  # Invalid date (in the past)
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date
        }
        tasks.append(task)
        return True
    except ValueError:
        return False  # Invalid date format

# Function to remove a task from the tasks list
def remove_task(tasks, description):
    tasks[:] = [task for task in tasks if task["description"] != description]
    return tasks

# Function to return the current list of tasks
def list_tasks(tasks):
    return tasks

# Function to save tasks to a CSV file
def save_tasks(tasks):
    with open("tasks.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["description", "priority", "due_date"])
        writer.writeheader()  # Write header
        writer.writerows(tasks)  # Write rows

# Function to load tasks from a CSV file
def load_tasks():
    tasks = []
    try:
        with open("tasks.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                task = {
                    "description": row["description"],
                    "priority": row["priority"],
                    "due_date": row["due_date"]
                }
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

# Entry point for the script
if __name__ == "__main__":
    main()





