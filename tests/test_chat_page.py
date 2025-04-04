import pytest
from unittest.mock import patch, MagicMock
import sys
import os
import streamlit as st

# Add the parent directory to path so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

# Create a more complete streamlit mock
mock_streamlit = MagicMock()
mock_components = MagicMock()
mock_streamlit.components = mock_components
sys.modules['streamlit'] = mock_streamlit
sys.modules['streamlit.components'] = mock_components



# Create a mock for the stop exception
class MockStopException(Exception):
    pass

# Replace st.stop with a function that raises our mock exception
st.stop = MagicMock(side_effect=MockStopException)
st.runtime = MagicMock()
st.runtime.scriptrunner = MagicMock()
st.runtime.scriptrunner.StopException = MockStopException

# Import your module after mocking
from functions import get_chatbot_response

# ---------- Test access control ----------
def test_access_without_login():
    # Clear session state
    if hasattr(st, 'session_state'):
        st.session_state = {}
    
    with pytest.raises(MockStopException):
        # Import the module which should check for login and call st.stop()
        with patch.dict('sys.modules', {'streamlit': st}):
            import Mental_Health_Companion
    
    # Verify user_email not in session state
    assert "user_email" not in st.session_state
# For test_fetch_chats
"""
@patch("Mental_Health_Companion.db_connection")
def test_fetch_chats(mock_db_conn):
    # Create mock data
    mock_chat_data = [
        {"role": "user", "message": "Hi"},
        {"role": "assistant", "message": "Hello!"}
    ]
    
    # Set up mock db connection
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = mock_chat_data
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn
    
    # Set up session state
    st.session_state = {"user_email": "test@example.com"}
    
    # Test directly what's happening in Mental_Health_Companion.py
    conn = mock_db_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_chats WHERE email = %s ORDER BY timestamp", (st.session_state['user_email'],))
    test_chats = cursor.fetchall()
    
    # Assertions
    assert isinstance(test_chats, list)
    assert len(test_chats) == 2
    assert test_chats[0]["message"] == "Hi"
    assert test_chats[1]["role"] == "assistant"
"""
"""
@patch("functions.get_chatbot_response")
@patch("Mental_Health_Companion.db_connection")
def test_chat_flow(mock_get_response, mock_db_conn):
    # Set up mocks - note the order matches the decorator order (bottom-up)
    mock_get_response.return_value = "I'm here to help you."
    
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn
    
    # Set up session state
    st.session_state = {
        "user_email": "test@example.com",
        "messages": [{"role": "user", "content": "I feel sad"}]
    }
    
    # Simulate user input
    user_prompt = "I feel anxious"
    
    # Add to session state
    st.session_state["messages"].append({"role": "user", "content": user_prompt})
    
    # Directly test the functionality
    conn = mock_db_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_chats (email, role, message) VALUES (%s, %s, %s)", 
                  (st.session_state["user_email"], "user", user_prompt))
    conn.commit()
    
    # Get chatbot response
    reply = mock_get_response(st.session_state["messages"])
    
    # Add to session state
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    
    # Store response
    conn = mock_db_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_chats (email, role, message) VALUES (%s, %s, %s)", 
                  (st.session_state["user_email"], "assistant", reply))
    conn.commit()
    
    # Assertions
    assert reply == "I'm here to help you."
    assert st.session_state["messages"][-1]["role"] == "assistant"
    assert st.session_state["messages"][-1]["content"] == "I'm here to help you." """
# For test_clear_chat_history

"""@patch("Mental_Health_Companion.db_connection")
def test_clear_chat_history(mock_db_conn):
    # Set up mocks
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn
    
    # Set up session state
    st.session_state = {
        "user_email": "test@example.com",
        "messages": [
            {"role": "user", "content": "hi"}, 
            {"role": "assistant", "content": "hello"}
        ]
    }
    
    # Simulate clearing chat
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi there! I'm your mental health companion. How can I help you?"}
    ]
    
    # Directly test database operation
    conn = mock_db_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_chats WHERE email = %s", (st.session_state["user_email"],))
    conn.commit()
    
    # Assertions
    assert len(st.session_state["messages"]) == 1
    assert cursor.execute.called
    assert conn.commit.called
    """