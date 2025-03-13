import json

def load_tasks(filename):
    try:
        with open("tasks.json", 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\n----- Task List -----")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def modify_tast_status(tasks, task_id, status):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = status
            print(f"Task {task_id} updated successfully!")
            return True
    print(f"Task {task_id} not found!")
    return False

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\n--- Task Statistics ---")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {round(average_priority, 2)}")

filename = 'tasks.json'
tasks = load_tasks(filename)

display_tasks(tasks)
calculate_statistics(tasks)
