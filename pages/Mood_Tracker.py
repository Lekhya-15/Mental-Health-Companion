import streamlit as st
from db_connection import db_connection
import datetime
from streamlit_calendar import calendar

def mood_to_color(mood):
    if mood == "Happy":
        return "#2ECC71"  # Green
    elif mood == "Sad":
        return "#3498DB"  # Blue
    elif mood == "Excited":
        return "#F39C12"  # Orange
    elif mood == "Stressed":
        return "#8E44AD"  # Purple
    elif mood == "Angry":
        return "#E74C3C"  # Dark Red
    else:
        return "#FFFFFF"

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
lottie_path = "/home/thania/Downloads/Joshi/Joshi/anime/moodtrack.json"

lottie_coding = load_lottiefile(lottie_path)
st.title('Mood Tracker')

# Layout: Create two columns for chat & animation
col1, col2 = st.columns([2, 1])  # Adjust ratio as needed

with col1:  # Main content (mood tracker)

        if 'user_email' not in st.session_state:
            st.warning('Please log in first')
        else:
            user_email = st.session_state['user_email']
            conn = db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT submitted_at, mood, mood_note FROM mood_tracker WHERE email = %s", (user_email,))
            mood_data = cursor.fetchall()
            conn.close()


            date_styles = {}
            # Store the color for each date

            date = st.date_input('Pick a date', min_value=datetime.date(2020, 1, 1), max_value=datetime.date.today())
            selected_mood = st.selectbox('How are you feeling today?', ['Happy', 'Sad', 'Excited', 'Stressed', 'Angry'])
            mood_note_exsisting="Enter how you feel..."
            calendar_events=[]
            for entry in mood_data:
                date_str = entry['submitted_at'].strftime("%Y-%m-%d")  # Convert to string format
                mood = entry['mood']
                color = mood_to_color(mood)
                date_styles[date_str] = color  
                
                if entry["submitted_at"]==date and entry["mood_note"]:
                    mood_note_exsisting=entry["mood_note"]
                calendar_events.append({
                "title": entry["mood_note"],
                "color": color,
                "start": date_str,
                "end": date_str,
                "resourceId": "a",
                })
            mood_note = st.text_input('Mood note',placeholder=mood_note_exsisting)
            if not mood_note and mood_note_exsisting!="Enter how you feel...":
                mood_note=mood_note_exsisting
            if st.button('Submit Mood'):
                conn = db_connection()
                cursor = conn.cursor()
                cursor.execute(f"""INSERT INTO mood_tracker (email, mood, mood_note, submitted_at) VALUES (%s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE mood = %s, mood_note = %s""",
                                (user_email, selected_mood, mood_note, date, selected_mood, mood_note))
                conn.commit()
                conn.close()
                st.success('Mood submitted successfully')
                st.rerun()
            
        

            # Prepare events based on fetched mood data
            
            # Calendar options
            calendar_options = {
                "editable": "true",
                "headerToolbar": {
                    "left": "prev,next",
                    "center": "title",
                    "right": ""
                },
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "dayGridMonth",
            }

            # Custom CSS to highlight the entire date box based on mood
            custom_css = """
            .fc-daygrid-day {
                position: relative;
            }
            """
            
            # Loop over each date and set background color for that day
            for date_str, color in date_styles.items():
                
                custom_css += f"""
                .fc-daygrid-day[data-date='{date_str}'] {{
                    background-color: {color} !important;
                }}
                """

        #     calendar_events = [
        #         {
        #         "title": "Event 1",
        #         "color": "#FF6C6C",
        #         "start": "2025-04-03",
        #         "end": "2025-04-05",
        #         "resourceId": "a",
        #     },
        #     {
        #         "title": "Event 2",
        #         "start": "2023-07-31T07:30:00",
        #         "end": "2023-07-31T10:30:00",
        #         "resourceId": "b",
        #     },
        #     {
        #         "title": "Event 3",
        #         "start": "2023-07-31T10:40:00",
        #         "end": "2023-07-31T12:30:00",
        #         "resourceId": "a",
        #     }
        # ]
            # Display the calendar with highlighted dates
            state = calendar(
                events=calendar_events,
                options=calendar_options,
                custom_css=custom_css,
                key="dayGrid"
            )
            mood_legend = {
                "Happy": "#2ECC71",
                "Sad": "#3498DB",
                "Excited": "#F39C12",
                "Stressed": "#8E44AD",
                "Angry": "#E74C3C"
            }

            st.markdown("### Mood Legend:")

            # st.markdown('<div style="display: inline-flex; justify-content: space-between; width: 100%;">', unsafe_allow_html=True)
            
            for mood, color in mood_legend.items():
                st.markdown(f'<div style="display: inline-flex; align-items: center; margin-right: 15px;">'
                            f'<div style="width: 15px; height: 15px; background-color: {color}; margin-right: 5px;"></div>'
                            f'<span style="font-size: 12px;">{mood}</span>'
                            f'</div>', unsafe_allow_html=True)
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
            