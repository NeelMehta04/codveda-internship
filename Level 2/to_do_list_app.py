import csv
import os

file_name = "Level 2/tasks.csv"

if not os.path.exists(file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["task", "done"])

def load_tasks():
    tasks = []
    with open(file_name, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append({"task": row["task"], "done": row["done"] == "True"})
    return tasks

def save_tasks(tasks):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["task", "done"])
        for task in tasks:
            writer.writerow([task["task"], task["done"]])

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Not Done"
        print(f"{i}. {t['task']} [{status}]")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    else:
        print("Invalid task number")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    else:
        print("Invalid task number")

while True:
    print("\n1. Add Task\n2. List Tasks\n3. Delete Task\n4. Mark Task as Done\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        try:
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        except ValueError:
            print("Invalid input")
    elif choice == '4':
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(index)
        except ValueError:
            print("Invalid input")
    elif choice == '5':
        break
    else:
        print("Invalid choice")