

import streamlit as st
from db_connection import db_connection
from functions import get_chatbot_response
st.set_page_config(page_title="Mental Health Companion")


# Import necessary libraries
from streamlit_lottie import st_lottie  
import json
import os

# File path to Lottie animation
lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/help.json"

# Function to load Lottie animation
def load_lottiefile(filepath: str):
    """Loads a Lottie animation from a JSON file."""
    if not os.path.exists(filepath):
        st.error(f"Error: File not found - {filepath}")
        return None
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile(lottie_path)

# Layout: Chat on the left, Animation on the right
col1, col2 = st.columns([2, 1])  # Adjust ratio for better alignment

with col1:
    st.title("Mental Health Companion")
    # Chatbot logic goes here...
    # Ensure user is logged in
if 'user_email' not in st.session_state:
    st.warning('Please log in first')
    st.stop()
else:
    user_email = st.session_state['user_email']

# Initialize chat history from the database
conn = db_connection()
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM user_chats WHERE email = %s ORDER BY timestamp", (user_email,))
chats = cursor.fetchall()
conn.close()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi there! I'm your mental health companion. How can I help you?"}]
    for chat in chats:
        role = "user" if chat["role"] == "user" else "assistant"
        st.session_state.messages.append({"role": role, "content": chat["message"]})

# Display chat history
for message in st.session_state.messages:
    if message["role"]=="assistant":
        with st.chat_message(message["role"],avatar="👨‍⚕️"):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# User input
prompt = st.chat_input("Say something")
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Store user message in database
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_chats (email, role, message) VALUES (%s, %s, %s)", (user_email, "user", prompt))
    conn.commit()
    conn.close()

    # Simulate assistant response (replace this with actual API call)
    # with st.spinner("Thinking..."):
    #     reply = "I'm here to support you. Can you tell me more about how you're feeling?"

    with st.spinner("Thinking..."):
        reply = get_chatbot_response(st.session_state.messages)

    # Display assistant response
    with st.chat_message("assistant",avatar="👨‍⚕️"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    # Store assistant response in database
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_chats (email, role, message) VALUES (%s, %s, %s)", (user_email, "assistant", reply))
    conn.commit()
    conn.close()

# Clear chat history
if st.button("Clear Chat History"):
    st.session_state.messages = [{"role": "assistant", "content": "Hi there! I'm your mental health companion. How can I help you?"}]

    # Delete chat history from database
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_chats WHERE email = %s", (user_email,))
    conn.commit()
    conn.close()

    st.rerun()

with col2:
    if lottie_coding:
        st_lottie(
            lottie_coding,
            speed=1,
            loop=True,
            height=250,  # Adjust height
            width=250,   # Adjust width
            quality="high",
            key="lottie_sidebar",
        )
