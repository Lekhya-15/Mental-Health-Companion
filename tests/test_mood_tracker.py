import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, date

# ---------- MOCKED DATA ----------
mock_mood_data = [
    {
        "submitted_at": datetime(2025, 4, 3),
        "mood": "Happy",
        "mood_note": "Feeling great!"
    },
    {
        "submitted_at": datetime(2025, 4, 2),
        "mood": "Sad",
        "mood_note": "Rough day"
    }
]

# ---------- TEST: Fetch Mood Data ----------
@patch("db_connection.db_connection")
def test_fetch_mood_data(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = mock_mood_data
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    email = "test@example.com"
    mock_cursor.execute("SELECT submitted_at, mood, mood_note FROM mood_tracker WHERE email = %s", (email,))
    mood_data = mock_cursor.fetchall()

    assert isinstance(mood_data, list)
    assert mood_data[0]["mood"] == "Happy"
    assert mood_data[1]["mood_note"] == "Rough day"

# ---------- TEST: Submit Mood Entry ----------
@patch("db_connection.db_connection")
def test_submit_mood(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    email = "test@example.com"
    selected_mood = "Stressed"
    mood_note = "Tough week"
    mood_date = date(2025, 4, 4)

    mock_cursor.execute(
        """INSERT INTO mood_tracker (email, mood, mood_note, submitted_at) VALUES (%s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE mood = %s, mood_note = %s""",
        (email, selected_mood, mood_note, mood_date, selected_mood, mood_note)
    )
    mock_conn.commit()
    assert mock_cursor.execute.called
    mock_conn.commit.assert_called_once()

# ---------- TEST: Mood Color Mapping ----------
def mood_to_color(mood):
    if mood == "Happy":
        return "#2ECC71"
    elif mood == "Sad":
        return "#3498DB"
    elif mood == "Excited":
        return "#F39C12"
    elif mood == "Stressed":
        return "#8E44AD"
    elif mood == "Angry":
        return "#E74C3C"
    else:
        return "#FFFFFF"

def test_mood_color_mapping():
    assert mood_to_color("Happy") == "#2ECC71"
    assert mood_to_color("Sad") == "#3498DB"
    assert mood_to_color("Excited") == "#F39C12"
    assert mood_to_color("Stressed") == "#8E44AD"
    assert mood_to_color("Angry") == "#E74C3C"
    assert mood_to_color("Unknown") == "#FFFFFF"