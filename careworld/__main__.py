from app.auth.login import login_page, get_profile
from utils.helpers import set_bg_hack
import streamlit as st

if __name__ == '__main__':
    st.set_page_config(layout="centered",
                       initial_sidebar_state="collapsed")
    # Hide menu and footers
    hide_streamlit_style = """

            <style>

            #MainMenu {visibility: hidden;}

            footer {visibility: hidden;}

            </style>

            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Load background image
    bg_image = 'careworld/images/background.png'
    set_bg_hack(bg_image)
    st.title('CareWorld')
    if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] == None:
        login_page()
    elif 'authentication_status' in st.session_state or st.session_state['authentication_status']:
        profile_view = get_profile()
        profile_view.view(st.session_state['name'].split(' ')[0], st.session_state['auth_obj'])
