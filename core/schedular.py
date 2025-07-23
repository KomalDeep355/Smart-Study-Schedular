from datetime import datetime, timedelta

def score_task(task):
    days_left = (datetime.strptime(task['deadline'], "%Y-%m-%d") - datetime.today()).days
    urgency = max(1, 10 - days_left)
    score = task['priority'] * 2 + urgency + task['difficulty']
    return score

def generate_schedule(tasks):
    tasks_sorted = sorted(tasks, key=score_task, reverse=True)
    schedule = []
    current_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

    for task in tasks_sorted:
        duration_hours = task['duration']
        end_time = current_time + timedelta(hours=duration_hours)
        schedule.append({
            'name': task['name'],
            'start_time': current_time.strftime("%Y-%m-%d %H:%M"),
            'duration': duration_hours,
            'end_time': end_time.strftime("%Y-%m-%d %H:%M")
        })
        current_time = end_time + timedelta(minutes=15)  # break

    return schedule
