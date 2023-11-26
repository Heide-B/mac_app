import streamlit as st
from utils.helpers import customize_widget
from datetime import datetime

def view(username: str, authenticator):
    with st.container():
        st.write(f'Welcome doctor: {username}!')
        st.divider()
    
    with st.container():
        with st.expander("Patient Briggs"):
            st.title("Current Annua Progres")
            st.progress(50,
            "Patient Briggs has completed 50% of her consulations and laboratory exam")

            tasks, status, next_due = st.columns([0.6, 0.2, 0.2])
            tasks.write("Consultation")
            status.warning("Upcoming")
            next_due.date_input(label="Upcoming Schedule", help="You can change /reschedule this task")
            st.divider()
        customize_widget("stExpander", "whit")

