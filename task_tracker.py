import sys
import json 
import os

TASK_FILE = 'tasks.json'

def ensure_task_file():   # Ensure the JSON file exists
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)
            
# Load tasks from the file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        # Reset the file if JSON is invalid or file not found
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
    
def add_task(title):   # Add a new task
    tasks = load_tasks()
    tasks_id = max([task["id"] for task in tasks], default=0) + 1
    tasks.append({"id": tasks_id, "title": title, "status": "not done"})
    save_tasks(tasks)
    print(f"Task added: {title}")
    
def list_tasks(filter_by=None):
    tasks = load_tasks()
    filtered_tasks = [
        task for task in tasks
        if filter_by is None or task["status"] == filter_by
    ]
    if not filtered_tasks:
        print("No tasks found.")
        return
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['title']} - {task['status']}")
        
def update_task(task_id, title): # Update a task
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] == title
            save_tasks(tasks)
            print(f"Task {task_id} upadated to: {title}")
            return
    print(f"Task {task_id} not found.")
    
def change_status(task_id, status):   # Change status of a task
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task {task_id} not found.")
    
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [tasks for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")
    
def main():      #CLI entry point
    ensure_task_file()
    if len(sys.argv) < 2:
        print("Usage: task_tracker.py [action] [parameters]")
        return
    
    action = sys.argv[1]
    
    if action == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif action == "list":
        filter_by = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(filter_by)
    elif action == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), " ".join(sys.argv[3]))
    elif action == "status" and len(sys.argv) > 3:
        change_status(int(sys.argv[2]), sys.argv[3])
    elif action == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    else:
        print("Invalid command or parameters.")
        
if __name__ == "__main__":
    main()