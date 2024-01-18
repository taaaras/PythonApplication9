import datetime

def log(message):
    print(f"[{datetime.datetime.now()}] {message}")

def log_creation_time(func):
    def wrapper(*args, **kwargs):
        task = func(*args, **kwargs)
        task['creation_time'] = datetime.datetime.now()
        log(f"Task '{task['title']}' created at {task['creation_time']}")
        return task
    return wrapper

def log_status_update(func):
    def wrapper(*args, **kwargs):
        task, new_status = func(*args, **kwargs)
        task['status'] = new_status
        task['update_time'] = datetime.datetime.now()
        log(f"Task '{task['title']}' updated to '{new_status}' at {task['update_time']}")
        return task, new_status
    return wrapper

tasks = []

@log_creation_time
def create_task(title, description):
    return {'title': title, 'description': description, 'status': 'new'}

@log_status_update
def update_task_status(task, new_status):
    return task, new_status

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log(f"Action '{func.__name__}' logged.")
        return result
    return wrapper

@log_action
def display_task_info(task):
    log(f"Task '{task['title']}': {task['description']}, Status: {task['status']}")

title = input("Enter task title: ")
description = input("Enter task description: ")
new_task = create_task(title, description)
tasks.append(new_task)

update_title = input("Enter task title to update status: ")
update_status = input("Enter new status: ")
for task in tasks:
    if task['title'] == update_title:
        updated_task, new_status = update_task_status(task, update_status)
        tasks.remove(task)
        tasks.append(updated_task)
        break

for task in tasks:
    display_task_info(task)