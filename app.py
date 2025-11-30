import streamlit as st
from utils import read_doc

read_doc()
st.title("Christmas exchange!")
with st.form("NameForm"):
    name = st.text_input(label="Enter the full first name of the sibling whose family or group you're a part of...")
    if st.form_submit_button():
        st.session_state["name"] = name.capitalize()
        st.switch_page("./pages/login.py")
