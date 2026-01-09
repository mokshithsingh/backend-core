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

def get_all_users() -> list[tuple[int, str, str]]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_email(email : str) -> tuple[int, str, str] | None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def delete_user_by_email(email : str) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE email = ?", (email,))
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows > 0

def update_user_email(old_email:str, new_email:str) -> bool: 
    conn = get_db_connection()
    cursor = conn.cursor()

    if old_email == new_email: 
        conn.close()
        return False
    
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (old_email,))
    if cursor.fetchone() is None : 
        conn.close()
        return False

    cursor.execute("SELECT 1 FROM users WHERE email = ?", (new_email,))

    if cursor.fetchone() is not None:
        conn.close()
        return False

    cursor.execute("UPDATE users SET email = ? WHERE email = ?", (new_email, old_email))
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows > 0