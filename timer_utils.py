import time
import csv
import pandas as pd
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


def load_history():
    """Charge l'historique sous forme de df"""
    try:
        df = pd.read_csv("history.csv", names=["Date", "Task", "Minutes"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Task", "Minutes"])