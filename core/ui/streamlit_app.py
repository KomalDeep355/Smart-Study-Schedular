import streamlit as st
from core.task_manager import add_task, delete_task, load_tasks
import matplotlib.pyplot as plt
import pandas as pd

def run_app(tasks, schedule):
    st.set_page_config(page_title="Smart Study Scheduler", layout="wide")
    st.title("📚 Smart Study Scheduler")
    st.sidebar.header("➕ Add New Task")
    with st.sidebar.form("task_form"):
        name = st.text_input("Task Name")
        subject = st.text_input("Subject")
        duration = st.number_input("Duration (hours)", min_value=0.5, max_value=8.0, step=0.5)
        deadline = st.date_input("Deadline")
        priority = st.slider("Priority", 1, 5, 3)
        difficulty = st.slider("Difficulty", 1, 5, 3)
        submitted = st.form_submit_button("Add Task")
        if submitted and name and subject:
            add_task(name, subject, duration, deadline.strftime('%Y-%m-%d'), priority, difficulty)
            st.success("✅ Task added! Please rerun to see it in schedule.")
    st.subheader("🗂️ Current Tasks")
    if tasks:
        df = pd.DataFrame(tasks)
        st.dataframe(df)
        task_ids = [task['id'] for task in tasks]
        delete_id = st.selectbox("Delete a Task (by ID)", options=task_ids)
        if st.button("🗑️ Delete Task"):
            delete_task(delete_id)
            st.success("Task deleted. Please rerun to update.")
    else:
        st.info("No tasks yet. Add one from the sidebar!")
    st.subheader("📅 Weekly Study Schedule")
    if schedule:
        schedule_df = pd.DataFrame(schedule)
        fig, ax = plt.subplots(figsize=(10, 5))
        for i, task in enumerate(schedule):
            start = pd.to_datetime(task['start_time'])
            ax.barh(task['name'], task['duration'], left=start.hour, color='skyblue')
        ax.set_xlabel("Hour of Day")
        ax.set_ylabel("Task")
        ax.set_title("Visualized Weekly Plan")
        st.pyplot(fig)
    else:
        st.warning("No schedule to display. Add tasks to see it here.")
