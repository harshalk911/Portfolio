import streamlit as st
from send_email import email_sender

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your Email")
    raw_message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: Portfolio App-Contact Form {user_email}


From: {user_email}
{raw_message}
"""
    if button:
        email_sender(message)
        st.info("Email was sent successfully!")
