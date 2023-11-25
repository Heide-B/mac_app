import streamlit_authenticator as stauth
import streamlit as st
from app.page_views import (
    doctor_view as doctor,
    parent_view as parent,
    patient_view as patient,
)
from utils.helpers import (
    customize_widget,
    modal_window,
    )
import yaml
from yaml.loader import SafeLoader

def login_page():
    with open('careworld/config/auth.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')
    customize_widget('stForm', 'white')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Successful login')
        st.session_state['username'] = username
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        new_reg = st.button('Not yet part of CareWorld? Sign Up!')
        if new_reg:
            _register_users(authenticator)

def _register_users(authenticator):
    # modal = Modal("User Registration", key='user_reg')
    # modal.open()
    modal = modal_window('user_reg','User Registration')
    with modal:
        authenticator.register_user('Register user', preauthorization=False)

def get_profile():
    profile_map = {
        'doctor': doctor,
        'parent': parent,
        'patient': patient,
    }
    with open('careworld/config/auth.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    username = st.session_state['username']
    profile = config['credentials']['usernames'][username]['profile']
    if profile in profile_map.keys():
        return profile_map[profile]
    else:
        st.error('USER HAS NO CONFIGURED PROFILE!')
        return None