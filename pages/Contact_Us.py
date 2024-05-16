import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email adress")
    subject = st.text_input("Subject")
    message = st.text_area("Enter your message")
    submit_button = st.form_submit_button(label="Send Email")
    if submit_button:
        st.write("Email has been sent")