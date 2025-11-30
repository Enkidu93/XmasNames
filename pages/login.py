import streamlit as st
from utils import read_doc, write_doc

read_doc()
if "name" not in st.session_state:
    st.switch_page("app.py")

if st.session_state["name"] in st.session_state["doc"]["names"] and "is_active" in st.session_state["doc"]["names"][st.session_state["name"]]:
    with st.form("LoginAgainForm"):
        passkey = st.text_input("It looks like you've already looked at your Xmas name. Enter the passphrase you created when first accessing the name.")
        if st.form_submit_button():
            if passkey == st.session_state["doc"]["names"][st.session_state["name"]]["passkey"]:
                st.session_state["logged_in"] = True
                write_doc()
                st.switch_page("./pages/name.py")
            else:
                st.error("Incorrect passphrase")
else:
    with st.form("LoginForm"):
        passkey = st.text_input("It looks like this is your first time looking at your Xmas name. Enter a passphrase to keep others from snooping.")
        if st.form_submit_button():
            st.session_state["doc"]["names"][st.session_state["name"]]["passkey"] = passkey
            st.session_state["doc"]["names"][st.session_state["name"]]["is_active"] = True
            st.session_state["logged_in"] = True
            write_doc()
            st.success("Passphrase saved!")
            st.switch_page("./pages/name.py")
