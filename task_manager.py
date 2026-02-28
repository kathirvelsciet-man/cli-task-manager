import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter description (optional): ")

    task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": title,
        "description": description,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"""
ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Created At: {task['created_at']}
Status: {status}
---------------------------""")

def complete_task(tasks):
    task_id = int(input("Enter task ID to complete: "))

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
            return

    print("Task not found!")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task not found!")

def main():
    tasks = load_tasks()

    while True:
        print("""
====== CLI Task Manager ======
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
