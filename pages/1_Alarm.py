import time
import streamlit as st
import datetime

st.title("Alarm App")

# Initialize alarmList in session state if not already present
if "alarmlist" not in st.session_state:
    st.session_state.alarmlist = []  # Initialize the list if it doesn't exist

# Time input
time_input = st.time_input("Set Alarm Time")


# Function to check if the current time matches any alarm time
def check_alarm():
    global alarmMessage
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for alarm_time in st.session_state.alarmlist:
            alarm_time_str = alarm_time.strftime("%H:%M")
            if now == alarm_time_str:
                alarmMessage.markdown(f"## :red[Alarm for {now} has reached!!]")
        time.sleep(1)


# Function to display the alarms and handle deletion
def write_alarms():
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, alarm_time in enumerate(st.session_state.alarmlist):
        col = cols[i % 3]
        col.title(f"Alarm: {alarm_time.strftime('%H:%M:%S')}")
        if col.button(f"Delete {i+1}"):
            st.session_state.alarmlist.pop(i)
            st.rerun()


# Set alarm button functionality
if st.button("Set Alarm"):
    if time_input not in st.session_state.alarmlist:
        st.session_state.alarmlist.append(time_input)
        st.success(f"Alarm set for {time_input.strftime('%H:%M:%S')}")
    else:
        st.warning("Alarm already set for this time")

alarmMessage = st.empty()
alarmMessage.markdown("## No Alarm Ringing")

# Display alarms
if st.session_state.alarmlist:
    st.write("Current Alarms:")
    write_alarms()
else:
    st.write("No alarms set yet.")

# Start the alarm checking in a separate thread to avoid blocking the UI
while True:
    check_alarm()
