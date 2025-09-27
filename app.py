import json
import streamlit as st
import pandas as pd
from timer_utils import start_timer, stop_timer, save_history, load_history

# Config Streamlit
st.set_page_config(page_title="Daily Timer", layout="wide")
st.title("Daily Timer")

# Charger les tâches
with open("tasks.json", "r") as f:
    tasks = json.load(f)

# Section tâches du jour
st.subheader("Tâches d'apprentissage du jour")
df_tasks = pd.DataFrame(tasks)
st.table(df_tasks)

# Sélection
task_names = [t["task"] for t in tasks]
selected_task = st.selectbox("Choisis une tâche :", task_names)

# Boutons Start / Stop côte à côte
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Timer"):
        st.session_state["start_time"] = start_timer()
        st.session_state["task"] = selected_task
        st.success(f"Timer démarré pour {selected_task}")

with col2:
    if st.button("Stop Timer"):
        if "start_time" in st.session_state:
            duration = stop_timer(st.session_state["start_time"])
            save_history(st.session_state["task"], duration)
            st.success(f"{st.session_state['task']} terminé en {duration:.2f} minutes")
            del st.session_state["start_time"]
            del st.session_state["task"]
        else:
            st.warning("Aucun timer en cours")

# Historique et progression
st.subheader("Progression")
history = load_history()

if not history.empty:
    # Minutes cumulées par tâche
    totals = history.groupby("Task")["Minutes"].sum().to_dict()

    for t in tasks:
        task = t["task"]
        goal = t["goal_minutes"]
        done = totals.get(task, 0)

        st.write(f"**{task}** : {done:.0f} / {goal} minutes")
        progress = min(int(done / goal * 100), 100)
        st.progress(progress)
else:
    st.info("Pas encore d'historique enregistré.")

# Historique détaillé dans un expander
with st.expander("Historique complet"):
    st.dataframe(history)

# Bouton pour tout nettoyer
if st.button("🗑️ Nettoyer tout l'historique"):
    open("history.csv", "w").close()
    st.success("Historique vidé")
    st.rerun()

# Supprimer une entrée spécifique
if not history.empty:
    st.subheader("Supprimer une entrée spécifique")

    # Créer un label lisible pour chaque ligne
    history["label"] = history.apply(
        lambda row: f"{row['Date']} | {row['Task']} | {row['Minutes']} min", axis=1
    )

    choice = st.selectbox("Choisis une entrée à supprimer :", history["label"])

    if st.button("Supprimer cette entrée"):
        # On garde toutes les lignes sauf celle choisie
        new_history = history[history["label"] != choice].drop(columns=["label"])
        new_history.to_csv("history.csv", index=False, header=False)
        st.success("Entrée supprimée")
        st.rerun()
