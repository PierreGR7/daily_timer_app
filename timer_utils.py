import time
import csv
from datetime import datetime

def start_timer():
    """ retourne le timestamp du début de la tâche """
    return time.time()

def stop_timer(start_time):
    """ calcule la durée écoulée en minutes"""
    end_time = time.time()
    duration = (end_time - start_time)/60
    return duration

def save_history(task, duration):
    """ Sauvegarde tasks et durée dans history.csv"""
    with open("history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.today().date(), task, round(duration, 2)])
