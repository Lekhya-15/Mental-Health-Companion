import streamlit as st
from db_connection import db_connection
import datetime
from streamlit_lottie import st_lottie
import json
import os

# Function to load Lottie animation
def load_lottiefile(filepath: str):
    if not os.path.exists(filepath):
        st.error(f"Error: File not found - {filepath}")
        return None
    with open(filepath, "r") as f:
        return json.load(f)

# File path to Lottie animation
lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/journal.json"
lottie_coding = load_lottiefile(lottie_path)
st.title('My Journals')

col1, col2 = st.columns([2, 1])  # Adjust width as needed

with col1:
        if 'user_email' not in st.session_state:
            st.warning('Please log in first')
        else:
            user_email = st.session_state['user_email']

            date = st.date_input('Pick a date for your journal entry', min_value=datetime.date(2020, 1, 1), max_value=datetime.date.today())
            journal_text = st.text_area('Write your journal for today',placeholder="Start writing here..")

            if st.button('Submit Journal'):
                conn = db_connection()
                cursor = conn.cursor()
                cursor.execute("""
            INSERT INTO user_journals (email, journal_text, submitted_at, journal_date) 
            VALUES (%s, %s, CURRENT_TIMESTAMP, %s)
            ON DUPLICATE KEY UPDATE email=email
        """, (user_email, journal_text, date))
                conn.commit()
                conn.close()
                st.success('Journal submitted successfully')
            conn = db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # Fetch all journals, ordered by date descending (latest first)
            cursor.execute("SELECT * FROM user_journals WHERE email = %s ORDER BY submitted_at DESC", (user_email,))
            journals = cursor.fetchall()
            conn.close()

            # Display journals
            # st.subheader("Your Journal Entries")
            
            # if journals:
            #     st.markdown("---") 
            #     for journal in journals:
            #         with st.container():
            #             delete_col = st.columns([8, 2])
            #             with delete_col[0]:
            #                 st.markdown("**Submitted At:** " + str(journal['submitted_at']))
            #                 st.markdown("**Journal Date:** " + str(journal['journal_date']))
            
                    
            #             with delete_col[1]:  # Place the button in the smaller column
            #                 if st.button(f"Delete", key=f"delete_{journal['submitted_at']}"):
            #                     conn = db_connection()
            #                     cursor = conn.cursor()
            #                     cursor.execute("DELETE FROM user_journals WHERE email = %s AND submitted_at = %s", (user_email, journal['submitted_at']))
            #                     conn.commit()
            #                     conn.close()
            #                     st.warning('Journal entry deleted.')
            #                     # st.experimental_rerun()
            #                     st.rerun()
            #             st.write(f"{journal['journal_text']}")
            #             st.markdown("---")  # Divider for clarity
            # else:
            #     st.write("🚀 You have no journal entries yet.")
            st.subheader("📚 Your Journal Entries")

            if journals:
                for journal in journals:
                    with st.container(border=True):
                        delete_col = st.columns([15, 2])
                        with delete_col[0]:
                            st.markdown(
                            f"""
                            <div style="border-radius: 10px; padding: 15px; background-color: #F0F2F6; margin-bottom: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                                <p style="font-size: 14px; color: black;"><b>Submitted At:</b> {journal['submitted_at']}</p>
                                <p style="font-size: 14px; color: black;"><b>Journal Date:</b> {journal['journal_date']}</p>
                                <p style="font-size: 14px; color: black;"><b>Journal Entry:</b> <br>{journal['journal_text']}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        # delete_col = st.columns([8, 2])
                        with delete_col[1]:  
                            if st.button("🚮", key=f"delete_{journal['submitted_at']}"):
                                conn = db_connection()
                                cursor = conn.cursor()
                                cursor.execute("DELETE FROM user_journals WHERE email = %s AND submitted_at = %s", (user_email, journal['submitted_at']))
                                conn.commit()
                                conn.close()
                                st.rerun()
            else:
                st.write("🚀 You have no journal entries")
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