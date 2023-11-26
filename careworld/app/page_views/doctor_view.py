import streamlit as st
from utils.helpers import customize_widget
from datetime import datetime

def view(username: str, authenticator):
    with st.container():
        st.title(f'Welcome doctor: {username}!')
        st.divider()
    
    with st.container():
        with st.expander("Patient Briggs"):
            st.title("Current Annua Progres")
            st.progress(50,
            "Patient Briggs has completed 50% of her consulations and laboratory exam")

            st.empty()
            tasks, status, next_due = st.columns([0.6, 0.2, 0.2])
            tasks.subheader("Consultation")
            status.warning("Upcoming")
            next_due.date_input(label="Upcoming Schedule", help="You can change /reschedule this task")
            st.divider()

            tasks2, status2, next_due2 = st.columns([0.6,0.2,0.2])
            tasks2.subheader("HbA1c Laborator")
            status2.success("Completed")
            next_due2.date_input(label="Upcoming Schedule",
            value=datetime(2023,2,14),
            help="You can change/reschedule this task"
            )
            st.divider()
        customize_widget("stExpander", "white")

