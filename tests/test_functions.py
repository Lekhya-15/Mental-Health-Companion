import pytest
from unittest.mock import patch, MagicMock
from functions import authenticate_user, get_chatbot_response

#Testing authenticate_user function

@patch("functions.db_connection")
def test_authenticate_user_success(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_cursor.fetchone.return_value = {
        "email": "test@example.com",
        "password": "testpass"
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    result = authenticate_user("test@example.com", "testpass")
    assert result == "test@example.com"

@patch("functions.db_connection")
def test_authenticate_user_wrong_password(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchone.return_value = {
        "email": "test@example.com",
        "password": "correctpass"
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    result = authenticate_user("test@example.com", "wrongpass")
    assert result == "Invalid password"

@patch("functions.db_connection")
def test_authenticate_user_not_found(mock_db_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_db_conn.return_value = mock_conn

    result = authenticate_user("unknown@example.com", "any")
    assert result == "User not found"

#Testing get_chatbot_response (mock API)

@patch("functions.requests.post")
def test_get_chatbot_response_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{
            "message": {
                "content": "This is a chatbot response."
            }
        }]
    }
    mock_post.return_value = mock_response

    response = get_chatbot_response([{"role": "user", "content": "How to relax?"}])
    assert "chatbot response" in response