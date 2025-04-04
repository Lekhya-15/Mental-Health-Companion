import os
from dotenv import load_dotenv
from db_connection import db_connection
from datetime import datetime

import requests
import json


def authenticate_user(email, password):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Query to get the user data from the database based on the email
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    # print(user)
    if user:
        # Check if the provided password matches the stored password
        if user['password'] == password:
            # Update last login time if password matches
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("UPDATE users SET last_login = %s WHERE email = %s", (current_time, email))
            conn.commit()  # Commit the update
            conn.close()
            return user['email']  # Authentication successful
        else:
            conn.close()
            return "Invalid password"  # Invalid password
    else:
        conn.close()
        return "User not found"

load_dotenv()

API_URL = "https://cloud.olakrutrim.com/v1/chat/completions"
api_key =  os.getenv("API_KEY")# Replace with your actual API key

def get_chatbot_response(user_messages):
    """Sends user messages to the chatbot API and retrieves the response."""
    messages=[{"role": "system", "content": "You are a helpful mental healt coach. User will ask questions related to mental health, yoga and meditation, your job is to answer to user questions politely ."}]
    messages.extend(user_messages)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "Meta-Llama-3.1-70B-Instruct",
        "messages": messages,  # Send full chat history
        "max_tokens": 1000
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    # print(response)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, there was an error getting a response."
