import streamlit as st

with st.form("user_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Welcome, {username}")