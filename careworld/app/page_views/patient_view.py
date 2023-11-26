import streamlit as st
from utils.helpers import customize_widget, modal_window
from datetime import datetime
import random

def view(username: str):
    with st.container():
        st.title(f'Welcome adventurer: {username}')
        st.divider()
    
    task_list = {
        "Doctor's Visit": {
            "widget": 'checkbox',
            "default": False,
            "due_date": datetime.today().date(),
            "pts": 50,
            "details": f"""Your last doctor's visit was on {datetime(2023,7,14).date()}.
                         Adventures have to visit a doctor every 3-6 months to
                           make sure your World is healthy, and to check what
                            achievements and animals you've collected.
                         """
        },
        "Blood Pressure Check": {
            "widget": 'number_input',
            "default": 0,
            "due_date": datetime.today().date(),
            "pts": 20,
            "details": f"""Your last Blood Pressure check was on {datetime(2023,7,14).date()}.
                        Everytime you visit your doctor, they need to make sure your heart is healthy!
                        Input your blood pressure to cross off this task.
                         """
        },
    }

    dailies = {
        "Check Blood Sugar": {
            "widget": 'number_input',
            "default": 0,
            "due_date": datetime.today().date(),
            "pts": 15,
            "details": f"""Check your blood sugar everyday before eating or right after you wake up!
                         """
        },
    }


    with st.container():
        with st.expander(':round_pushpin: Main Adventure', True):
            task_list = _create_task(task_list)
            info = {k: task_list[f"{k.split('details')[1].split('-')[1].split('_')[0]}"]['details'] for k, v in st.session_state.items() if "details" in k \
                     and k.split('details')[1].split('-')[1].split('_')[0] in task_list.keys()\
                        and v == True}
            completed = {k: task_list['completed'] for k, v in task_list.items() \
                         if "completed" in v.keys() }

            if len(info) > 0:
                modal = modal_window('main adv', 'Task Details')
                modal.write(list(info.values())[0])
        customize_widget('stExpander', 'white')

    with st.container():
        with st.expander(':four_leaf_clover: Daily Adventures', True):
            dailies = _create_task(dailies)
            info = {k: dailies[f"{k.split('details')[1].split('-')[1].split('_')[0]}"]['details'] for k, v in st.session_state.items() if "details" in k \
                     and k.split('details')[1].split('-')[1].split('_')[0] in dailies.keys()\
                     and v == True}
            completed = {k: dailies[f"{k.split('checker')[1].split('-')[1].split('_')[0]}"]['checker'] for k, v in st.session_state.items() if "checker" in k \
                     and k.split('checker')[1].split('-')[1].split('_')[0] in dailies.keys()\
                     and v not in [0, None, False]}
            
            if len(info) > 0:
                modal = modal_window('dail', 'Task Details')
                modal.write(list(info.values())[0])

        customize_widget('stExpander', 'white')

def _create_task(task_list: dict):
    widgets = {
        'number_input': st.number_input,
        'checkbox': st.checkbox,
        'text_input': st.text_input,
    }   

    for name, values in task_list.items():
        key = values['widget']+'-'+name+'_'+str(random.randint(1,1000))
        with st.container():
            show_details = st.toggle('Task info', help='Enable to show details about this task!',
                                        key='details'+key)
            check = widgets[values['widget']](name, value=values['default'], key='checker'+key)
            st.warning(f'Due Date {values["due_date"]}', icon='🧭')
            st.info(f'{values["pts"]}seeds', icon='🌱')
            st.divider()
        if check not in [0, False, None]:
            task_list = _update_value(task_list, name)

    return task_list

@st.cache_data
def _update_value(task_list: dict, name: str):
    task_list[name]['complete'] = True

    return task_list