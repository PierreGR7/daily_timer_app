import json
from timer_utils import start_timer, save_history

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
