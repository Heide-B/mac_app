import streamlit as st

def view(username: str, authenticator):
    with st.container():
        st.write(f'Welcome doctor: {username}!')
        st.divider()
    
    with st.container():
        with st.expander("Patient Briggs"):
            st.title("Current Annua Progres")
            st.progress(50)

