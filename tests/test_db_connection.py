from db_connection import db_connection

def test_connection():
    conn = db_connection()
    assert conn.is_connected()
    conn.close()