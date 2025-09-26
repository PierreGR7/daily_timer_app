import json
import streamlit as st
import pandas as pd
from timer_utils import start_timer, stop_timer, save_history

with open("tasks.json", "r") as f:
    tasks = json.load(f)

st.title("Daily Timer")

st.subheader("Tâches du jour")
for t in tasks:
    st.write(f"- {t['task']} (objectif {t['goal_minutes']} min)")

task_names=[t["task"] for t in tasks]
selected_task = st.selectbox("Choisis une tâche :", task_names)

if st.button("Start Timer"):
    st.session_state["start_time"] = start_timer()
    st.session_state["task"] = selected_task
    st.success(f"Timer démarré pour {selected_task}")

if st.button("STOP"):
    if "start_time" in st.session_state:
        duration = stop_timer(st.session_state["start_time"])
        save_history(st.session_state["task"], duration)
        st.success(f"{st.session_state['task']} terminée en {duration:.2f} minutes")
        del st.session_state["start_time"]
        del st.session_state["task"]
    else:
        st.warning("Aucun timer en cours")

if st.button("View History"):
    history = pd.read_csv("history.csv")
    st.dataframe(history)

if st.button("Clear History"):
    history = pd.read_csv("history.csv")
    history.drop(index=0, inplace=True)
    history.to_csv("history.csv", index=False)
    st.success("Historique vidé")