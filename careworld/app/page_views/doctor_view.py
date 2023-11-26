import streamlit as st
from utils.helpers import customize_widget
from datetime import datetime

def view(username: str, authenticator):
    with st.container():
        st.title(f'Welcome Doctor: {username}!')
        authenticator.logout('Logout', 'main')
        st.divider()

    task_list = {
        "Physician Consultation": {
            "status": 'Upcoming',
            "date": datetime.today().date(),
        },
        "HbA1c Laboratory": {
            "status": 'Completed',
            "date": datetime(2024, 2, 14).date(),
        },
    }

    with st.container():
        with st.expander("Patient Briggs"):
            st.title("Current Annual Progress")
            st.progress(50,
            "Patient Briggs has completed 50% of their consulations and laboratory exam")

            _create_task(task_list)
            task_list = _add_task(task_list)
        customize_widget("stExpander", "white")

def _create_task(task_list: dict):
    statuses = {
        'Completed': st.success,
        'Upcoming': st.warning,
        'Late': st.error,
    }

    with st.container():
        for name, values in task_list.items():
            st.subheader(name)
            statuses[values['status']](values["status"])
            st.date_input(label="Upcoming Schedule", 
                                value=values['date'],
                                help="You can reschedule this checkpoint")
            st.divider()

def _add_task(task_list: dict):
    tasks = {'Consultation': ['Eye Exam','BMI','Dental Exam','Foot Exam','Physician Consult'],
             'Laboratory': ['HbA1c', 'Triglyceride', 
                            'Total Cholesterol','LDL Chol','HDL Chol',
                            'Albumin-Crea Ratio','ECG'],
             None: []
             }
    create = st.button('Create New Checkpoint', use_container_width=True)

    if create:
        with st.form('Add Checkpoint Details'):
            task_type = st.selectbox('Checkpoint Type',
                        ['Consultation','Laboratory'])
            task_detail = st.selectbox('Checkpoint Detail',
                                    tasks[task_type])
            due_date = st.date_input('Scheduled Date')
            submitted = st.form_submit_button("Create")
            delta = due_date - datetime.today().date()
            if delta.days >= 31:
                status =  'Completed'
            elif delta.days <= 0:
                status = 'Late'
            else:
                status = 'Upcoming'

            if submitted:
                task_list[f'{task_detail} {task_type}'] = {
                    "status": status,
                    "date": due_date
                }
            
    return task_list
