import streamlit as st
import json
import random

def update_names():
    giver_names = list()
    given_names = list()
    names = list(set(st.session_state["doc"]["names"]).difference(set(["Santa"])))
    done = False
    print(names)
    while not done:
        print("Refreshing names")
        for giver_name in names:
            giver_names.append(giver_name)
            given_name = random.choice(names)
            i = 0
            while (given_name in given_names or given_name == giver_name) and i < 50:
                i += 1
                given_name = random.choice(names)
            if i > 50:
                done = False
            else:
                given_names.append(given_name)
                done = len(given_names) == len(names)
                st.session_state["doc"]["names"][giver_name]["has"] = given_name
    write_doc()

def write_doc():
    with open('./data.json', 'w') as f:
        f.write(json.dumps(st.session_state["doc"]))

def read_doc():
    with open('./data.json', 'r') as f:
        contents = f.read()
        if contents.strip() == "":
            contents = "{}"
        doc = json.loads(contents)
        st.session_state["doc"] = doc