import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
) 

import streamlit as st
import pandas as pd
from datetime import datetime

# Configure the app
st.title("Faculty Time Slot Selection")
st.write("Please select your preferred time slots for Technical Rehearsal for the Week of March 30-April 03 .")

# Available Slots
available_slots = [
    "Monday 09:00 - 10:00",
    "Monday 10:00 - 11:00",
    "Monday 11:00 - 12:00",
    "Monday noon -1:00 pm",
    "Monday 1:00 pm -2:00 pm",
    "Monday 2:00 pm - 3:00 pm",
    "Monday 3:00 pm - 4:00 pm",
    "Monday 4:00 pm - 5:00 pm",
    "Tuesday 09:00 - 10:00",
    "Tuesday 10:00 - 11:00",
    "Tuesday 11:00 - 12:00",
    "Tuesday noon -1:00 pm",
    "Tuesday 1:00 pm -2:00 pm",
    "Tuesday 2:00 pm - 3:00 pm",
    "Tuesday 3:00 pm - 4:00 pm",
    "Tuesday 4:00 pm - 5:00 pm",
    "Wednesday 09:00 - 10:00",
    "Wednesday 10:00 - 11:00",
    "Wednesday 11:00 - 12:00",
    "Wednesday noon -1:00 pm",
    "Wednesday 1:00 pm -2:00 pm",
    "Wednesday 2:00 pm - 3:00 pm",
    "Wednesday 3:00 pm - 4:00 pm",
    "Wednesday 4:00 pm - 5:00 pm",
    "Thursday 09:00 - 10:00",
    "Thursday 10:00 - 11:00",
    "Thursday 11:00 - 12:00",
    "Thursday noon -1:00 pm",
    "Thursday 1:00 pm -2:00 pm",
    "Thursday 2:00 pm - 3:00 pm",
    "Thursday 3:00 pm - 4:00 pm",
    "Thursday 4:00 pm - 5:00 pm",
    "Friday 09:00 - 10:00",
    "Friday 10:00 - 11:00",
    "Friday 11:00 - 12:00",
    "Friday noon -1:00 pm",
    "Friday 1:00 pm -2:00 pm",
    "Friday 2:00 pm - 3:00 pm",
    "Friday 3:00 pm - 4:00 pm",
    "Friday 4:00 pm - 5:00 pm"
]

# Faculty input
Faculty_name = st.text_input("Enter your name:")
selected_slots = st.multiselect("Select your top preferences:", available_slots)
# Save functionality
if st.button("Submit Preferences"):
    if Faculty_name and selected_slots:
        # Create a dictionary to hold data
        data = {"Faculty": Faculty_name, "Preferences": [", ".join(selected_slots)]}
        df = pd.DataFrame(data)
        
        # Save to CSV (or update a shared database)
        df.to_csv("time_slots.csv", mode='a', header=False, index=False)
        st.success(f"Saved {Faculty_name}'s preferences!")
    else:
        st.error("Please enter your name and select at least one slot.")

# Optional: Display submitted data
if st.checkbox("Show all submissions"):
    try:
        df_view = pd.read_csv("time_slots.csv", names=["Faculty", "Preferences"])
        st.dataframe(df_view)
    except FileNotFoundError:
        st.write("No submissions yet.")
