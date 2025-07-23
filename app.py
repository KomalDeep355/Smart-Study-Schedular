from core.task_manager import load_tasks
from core.scheduler import generate_schedule
from ui.streamlit_app import run_app

def main():
    tasks = load_tasks()
    schedule = generate_schedule(tasks)
    run_app(tasks, schedule)

if __name__ == "__main__":
    main()
