import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email address")
    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: New email from {user_email} 

From: {user_email}
{raw_message}
"""

    submit_button = st.form_submit_button(label="Send Email")

    if submit_button:
        send_email(message)
        st.success("Email sent successfully")
