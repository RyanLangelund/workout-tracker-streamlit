import streamlit as st

st.title("Workout Tracker")

name = st.text_input("Enter your name")
exercise = st.text_input("Exercise")
sets = st.number_input("Sets", min_value=0)
reps = st.number_input("Reps", min_value=0)
weight = st.number_input("Weight", min_value=0)

if st.button("Save Workout"):
    st.write("Workout Saved!")
    st.write(name, exercise, sets, reps, weight)