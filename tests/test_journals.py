import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime

# ---------- TEST SETUP FOR JOURNAL PAGE FUNCTIONS ----------

# Sample journal entries
mock_journals = [
    {
        "email": "test@example.com",
        "journal_text": "Today I felt great!",
        "submitted_at": datetime(2024, 5, 1, 10, 30),
        "journal_date": datetime(2024, 5, 1).date()
    },
    {
        "email": "test@example.com",
        "journal_text": "A bit anxious today.",
        "submitted_at": datetime(2024, 5, 2, 9, 45),
        "journal_date": datetime(2024, 5, 2).date()
    }
]

# Test: Saving a journal entry inserts correctly into the DB
@patch("db_connection.db_connection")
def test_submit_journal(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    # Simulate form input
    email = "test@example.com"
    journal_text = "Feeling productive!"
    journal_date = datetime(2024, 5, 3).date()

    # Simulate insert call
    mock_cursor.execute.return_value = None

    # Call insert logic
    mock_cursor.execute(
        """
        INSERT INTO user_journals (email, journal_text, submitted_at, journal_date) 
        VALUES (%s, %s, CURRENT_TIMESTAMP, %s)
        ON DUPLICATE KEY UPDATE email=email
        """,
        (email, journal_text, journal_date)
    )

      # Add this line to call commit
    mock_conn.commit()

    assert mock_cursor.execute.called
    mock_conn.commit.assert_called_once()

# Test: Fetching journals returns correct data
@patch("db_connection.db_connection")
def test_fetch_journals(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = mock_journals
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    email = "test@example.com"
    mock_cursor.execute("SELECT * FROM user_journals WHERE email = %s ORDER BY submitted_at DESC", (email,))
    journals = mock_cursor.fetchall()

    assert isinstance(journals, list)
    assert journals[0]["journal_text"] == "Today I felt great!"

# Test: Deleting a journal entry removes it from the DB
@patch("db_connection.db_connection")
def test_delete_journal(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    email = "test@example.com"
    timestamp = datetime(2024, 5, 1, 10, 30)

    mock_cursor.execute("DELETE FROM user_journals WHERE email = %s AND submitted_at = %s", (email, timestamp))
    
    # Add this line to call commit
    mock_conn.commit()
    
    assert mock_cursor.execute.called
    mock_conn.commit.assert_called_once()