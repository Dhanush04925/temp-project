import streamlit as st
from pymongo import MongoClient

# Helper to connect to Mongo
def get_db():
    client = MongoClient(st.secrets["mongo"]["uri"])
    return client.CanteenDB

st.title("Smart Canteen Management System")

# App Details Section
st.markdown("""
### About the App
This system uses AI to predict canteen demand and automates inventory management via MongoDB Cloud.
""")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Registration"])

    with tab1:
        email = st.text_input("Email")
        pw = st.text_input("Password", type="password")
        if st.button("Login"):
            user = get_db().users.find_one({"email": email, "password": pw})
            if user:
                st.session_state.logged_in = True
                st.success("Logged in! Use the sidebar to access tools.")
                st.rerun()
            else:
                st.error("Invalid credentials.")

    with tab2:
        st.subheader("Register New User")
        with st.form("reg_form"):
            new_name = st.text_input("Name")
            new_email = st.text_input("Email")
            new_pw = st.text_input("Password", type="password")
            if st.form_submit_button("Register"):
                get_db().users.insert_one({"name": new_name, "email": new_email, "password": new_pw})
                st.success("Registered to MongoDB Cloud! You can now login.")
else:
    st.write(f"### Welcome back!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()