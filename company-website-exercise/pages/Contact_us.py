import streamlit as st
from send_email import send_email

st.header("Contact us!")

with st.form("contact_us_form"):
    user_email = st.text_input("Your Email Address")
    topic_to_discuss = st.selectbox("What topic do you want to discuss?", options=('Job Inquiries', 'Project Proposals', 'Other'))
    st.write(f"You selected: {topic_to_discuss}")
    raw_message = st.text_area(label='Write down here your message')
    submit_button = st.form_submit_button("Submit")
    message_to_send = f"""\
Subject: New email from {user_email}
    
Subject: {topic_to_discuss}
{raw_message}
"""

    if submit_button: 
        send_email(message=message_to_send)
        st.info("Your email was sent succesfully!")

    
    
st.session_state