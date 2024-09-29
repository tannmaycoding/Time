import streamlit as st
import time

st.title("Stopwatch")

# Initialize session state for watch time
if "watch_time" not in st.session_state:
    st.session_state.watch_time = 0

col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
# Create a placeholder for the time display
time_display = col2.empty()

# Initial display
time_display.markdown(f"## {st.session_state.watch_time} sec")

# Create buttons for Start, Stop, and Reset
start = col1.button("Start", use_container_width=True)
stop = col2.button("Stop", use_container_width=True)
reset = col3.button("Reset", use_container_width=True)

if start:
    while not stop and not reset:
        st.session_state.watch_time += 0.01
        st.session_state.watch_time = round(st.session_state.watch_time, 2)

        # Update the time display
        time_display.markdown(f"## {st.session_state.watch_time} sec")

        # Pause briefly to allow the stopwatch to tick
        time.sleep(0.01)  # Adjust this for faster/slower ticking

if reset:
    st.session_state.watch_time = 0
    time_display.markdown("## 0.00 sec")  # Reset display
