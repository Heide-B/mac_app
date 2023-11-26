import streamlit as st
import streamlit.components.v1 as components
import base64

def set_bg_hack(image_path):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(image_path, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def customize_widget(widget: str, color: str):
    css="""
            <style>
                [data-testid="{widget}"]
        """.format(widget=widget)
    css += " {"
    css += """
                background: {color};
            """.format(color=color)
    css += """
                    }
                </style>
            """

    st.markdown(css, unsafe_allow_html=True)

def modal_window(key: str,
                 title: str
                 ):
    st.markdown(
        f"""
        <style>
        div[data-modal-container='true'][key='{key}'] {{
            position: absolute; 
            width: 100vw !important;
            left: 0;
            z-index: 99992;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}

        div[data-modal-container='true'][key='{key}'] > div:first-child {{
            margin: auto;
        }}

        div[data-modal-container='true'][key='{key}'] h1 a {{
            display: none
        }}

        div[data-modal-container='true'][key='{key}']::before {{
                position: fixed;
                content: ' ';
                left: 0;
                right: 0;
                top: 0;
                bottom: 0;
                z-index: 100;
                background-color: rgba(0, 0, 0, 0.5);
        }}
        div[data-modal-container='true'][key='{key}'] > div:first-child {{
            max-width: 544px;
        }}

        div[data-modal-container='true'][key='{key}'] > div:first-child > div:first-child {{
            width: unset !important;
            background-color: #fff;
            padding: 10px;
            margin-top: 5px;
            margin-left: -20px;
            margin-right: -20px;
            margin-bottom: -40px;
            z-index: 1001;
            border-radius: 5px;
        }}
        div[data-modal-container='true'][key='{key}'] > div:first-child > div:first-child > div:first-child  {{
            overflow-y: hidden;
            max-height: 70vh;
            overflow-x: hidden;
            max-width: 544px;
        }}
        
        div[data-modal-container='true'][key='{key}'] > div > div:nth-child(2)  {{
            z-index: 1003;
            position: absolute;
        }}
        div[data-modal-container='true'][key='{key}'] > div > div:nth-child(2) > div {{
            text-align: right;
            padding-right: 20px;
            max-width: 744px;
        }}

        div[data-modal-container='true'][key='{key}'] > div > div:nth-child(2) > div > button {{
            right: 0;
            margin-top: 54px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        _container = st.container()
        _container.markdown(
            f"<h2>{title}</h2>", unsafe_allow_html=True)

        close_ = st.button('X', key=f'{key}-close')
        if close_:
            st.rerun()

    components.html(
        f"""
        <script>
        // STREAMLIT-MODAL-IFRAME-{key} <- Don't remove this comment. It's used to find our iframe
        const iframes = parent.document.body.getElementsByTagName('iframe');
        let container
        for(const iframe of iframes)
        {{
        if (iframe.srcdoc.indexOf("STREAMLIT-MODAL-IFRAME-{key}") !== -1) {{
            container = iframe.parentNode.previousSibling;
            container.setAttribute('data-modal-container', 'true');
            container.setAttribute('key', '{key}');
        }}
        }}
        </script>
        """,
        height=0, width=0
    )
    return _container
