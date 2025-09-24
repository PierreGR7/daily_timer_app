import time
import csv
import json
from datetime import datetime

def start_timer(task):
    print(f"⏳ Starting {task}... (press Enter to stop)")
    start = time.time()
    input()
    end = time.time()
    duration = (end - start) / 60  # minutes
    print(f"{task} done: {duration:.2f} minutes")
    return duration

def save_history(task, duration):
    with open("history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.today().date(), task, round(duration, 2)])

if __name__ == "__main__":

    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    print("📋 Tâches du jour :")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} (objectif {t['goal_minutes']} min)")

    choice = int(input("Choisis une tâche (numéro) : "))
    selected_task = tasks[choice - 1]["task"]

    duration = start_timer(selected_task)
    save_history(selected_task, duration)
