import streamlit as st

from utils import read_doc, update_names

if "logged_in" not in st.session_state or "name" not in st.session_state:
    st.switch_page('app.py')

read_doc()
if "has" not in st.session_state["doc"]["names"][st.session_state["name"]]:
    st.error("Something went wrong!")
else:
    given_name = st.session_state["doc"]["names"][st.session_state["name"]]["has"]
    if given_name == "Anggel":
        given_name = "Anggel and Meili"
    st.text(f"{st.session_state['name']}'s group has {given_name}'s group!")
    st.snow()

if st.session_state["name"] == "Santa":
    if st.button("Refresh names"):
        update_names()
    if st.button("Show names"):
        st.code(st.session_state["doc"])
