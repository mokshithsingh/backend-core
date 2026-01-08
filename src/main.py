from src.db.database import get_db_connection
from src.db.schema import create_tables
from src.services.user_service import create_user

def main():
    create_tables()

    username = input("Enter your username: ")
    email = input("Enter your email: ")

    if create_user(username, email) : 
        print("User created successfully.")
    else: 
        print("A user with this email already exists.")
    
if __name__ == "__main__":
    main()
