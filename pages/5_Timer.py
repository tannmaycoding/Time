import streamlit as st
import time as t

st.title("Timer")
duration = st.text_input("Time duration (in seconds)")
if "duration" not in st.session_state:
    st.session_state.duration = 0

col1, col2, col3 = st.columns(3, vertical_alignment="bottom")

if col2.button("Set Timer"):
    st.session_state.duration = int(duration)

time = col2.empty()
time.markdown(f"## {st.session_state.duration} sec")


start = col1.button("Start", use_container_width=True)
stop = col2.button("Stop", use_container_width=True)
reset = col3.button("Reset", use_container_width=True)

if start:
    while not stop and not reset:
        if st.session_state.duration > 0:
            st.session_state.duration -= 1
            time.markdown(f"## {st.session_state.duration} sec")
            t.sleep(1)

        else:
            time.markdown("### :red[TIMER HAS ENDED]")
            break

if reset:
    time.markdown("## 0 secs")
