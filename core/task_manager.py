import json
import uuid
from datetime import datetime

TASKS_FILE = 'data/tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(name, subject, duration, deadline, priority, difficulty):
    tasks = load_tasks()
    new_task = {
        'id': str(uuid.uuid4())[:8],
        'name': name,
        'subject': subject,
        'duration': duration,
        'deadline': deadline,
        'priority': priority,
        'difficulty': difficulty
    }
    tasks.append(new_task)
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
