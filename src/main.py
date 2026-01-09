from src.db.schema import create_tables
from src.services.user_service import create_user, get_all_users, get_user_by_email, delete_user_by_email, update_user_email

def main():
    create_tables()

    q1 = input("Do you want to create a new user? (y/n): ")
    if q1.lower() == 'y':
        username = input("\nEnter your username: ")
        email = input("Enter your email: ")

        if create_user(username, email) : 
            print("User created successfully.")
        else: 
            print("A user with this email already exists.")

    q2 = input("\nDo you want to see all users? (y/n): ")
    if q2.lower() == 'y':
        print("\nAll users in the system:")
        users = get_all_users()
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    q3 = input("\nDo you want to get a user by email? (y/n): ")
    if q3.lower() == 'y':
        email = input("\nEnter the email of the user you want to retrieve: ")
        user = get_user_by_email(email)
        if user:
            print(f"User found: ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        else:
            print("User not found.")

    q4 = input("\nDo you want to delete a user by email? (y/n): ")
    if q4.lower() == "y":
        email = input("\nEnter the email of the user you want to delete: ")
        if delete_user_by_email(email):
            print("User deleted successfully.")
        else:
            print("User not found or could not be deleted.")

    q5 = input("\nDo you wwant to update a user's email? (y/n): ")
    if q5.lower() == "y": 
        old_email = input("\nEnter the current email of the user: ")
        new_email = input("Enter the new email of the user")
        if update_user_email(old_email, new_email): 
            print("User email updated successfully.")
        else: 
            print("User not found or email coud not be updated.")

if __name__ == "__main__":
    main()
