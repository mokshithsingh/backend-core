from src.db.database import get_db_connection

def create_user(username: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    exists = cursor.fetchone() is not None

    if exists:
        conn.close()
        return False
    else:
        cursor.execute(
            "INSERT INTO users(name, email) VALUES (?, ?)", (username, email)
        )
        conn.commit()
        conn.close()
        return True
