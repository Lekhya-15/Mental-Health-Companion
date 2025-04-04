import streamlit as st
from db_connection import db_connection
from functions import authenticate_user
import datetime
import re
# Login page
# def login_page():
#     st.title('Login')
#     email = st.text_input('Email')
#     password = st.text_input('Password', type='password')

#     if st.button('Login'):
#         if email and password:
#             user = authenticate_user(email, password)
#             print(user)
#             if user==email:
#                 st.success('Login Successful')
#                 st.session_state['user_email'] = email  # Store user info in session
#                 # st.experimental_rerun()
#             else:
#                 st.error('Invalid email or password')
#         else:
#             st.error('Please enter both email and password')
def login_page():
    st.title('Login/SignUp')
     
    # Check if user is already logged in
    if 'user_email' in st.session_state:
        st.write(f"Logged in as: {st.session_state['user_email']}")
        if st.button('Logout'):
            logout_user()
        return  # Exit the function if already logged in
    
    # Tabs for Login and Create Account
    tab1,tab2 = st.tabs(["Login", "Sign Up"])

    # Login Tab
    with tab1:
        email = st.text_input('Registered Email', placeholder="Enter your email")
        password = st.text_input('Password',type='password', placeholder="Enter your password")


        if st.button('Login'):
            if email and password:
                user = authenticate_user(email, password)
                if user==email:
                    st.success('Login Successful')
                    st.session_state['user_email'] = email  # Store user info in session
                    # st.experimental_rerun()
                else:
                    st.error('Invalid email or password')
            else:
                st.error('Please enter both email and password')



# Create Account Tab
    with tab2:
        new_email = st.text_input('Email')
        new_password = st.text_input('New Password', type='password')
        confirm_password = st.text_input('Confirm Password', type='password')

        if st.button('Sign Up'):
            if new_email and new_password and confirm_password:
                # Check if the email is a valid Gmail account
                gmail_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
                if re.match(gmail_pattern, new_email):
                    if new_password == confirm_password:
                        conn = db_connection()
                        cursor = conn.cursor()

                    # Check if the email already exists
                        cursor.execute("SELECT email FROM users WHERE email = %s", (new_email,))
                        existing_user = cursor.fetchone()

                        if existing_user:
                            st.error('An account with this email already exists.')
                        else:
                        # Insert new user into database
                            cursor.execute("INSERT INTO users (email, password, created_at, last_login) VALUES (%s, %s, NOW(), NOW())",
                                       (new_email, new_password))
                            conn.commit()
                            conn.close()
                            message = f'Account for {new_email} created successfully! Please log in.'
                            st.success(message)
                    else:
                        st.error('Passwords do not match.')
                else:
                    st.error('Please enter a valid Gmail account.')
            else:
                st.error('Please fill in all fields.')


def logout_user():
    # Clear the session state
    if 'user_email' in st.session_state:
        del st.session_state['user_email']
    st.success("You have been logged out successfully")
    # Optional: Force a rerun to refresh the page
    #st.experimental_rerun()





# def calendar_page():
#     st.title('Calendar Interface')

#     if 'user_email' not in st.session_state:
#         st.warning('Please log in first')
#     else:
#         user_email = st.session_state['user_email']

#         date = st.date_input('Pick a date', min_value=datetime.date(2020, 1, 1), max_value=datetime.date.today())
#         mood = st.selectbox('How are you feeling today?', ['Happy', 'Sad', 'Excited', 'Stressed', 'Angry'])
#         mood_note = st.text_area('Mood note')

#         if st.button('Submit Mood'):
#             conn = db_connection()
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO mood_tracker (email, mood, mood_note, submitted_at) VALUES (%s, %s, %s, %s) "
#                            "ON DUPLICATE KEY UPDATE mood = %s, mood_note = %s",
#                            (user_email, mood, mood_note, date, mood, mood_note))
#             conn.commit()
#             conn.close()
#             st.success('Mood submitted successfully')
#         # show_calendar(user_email)

st.set_page_config(page_title="Home")
login_page()
