import time
import csv
from datetime import datetime

def start_timer(task):
    print(f"⏳ Starting {task}... (press Enter to stop)")
    start = time.time()
    input()
    end = time.time()
    duration = (end - start) / 60  # minutes
    print(f"✅ {task} done: {duration:.2f} minutes")
    return duration

def save_history(task, duration):
    with open("history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.today().date(), task, round(duration, 2)])
