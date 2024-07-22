# app.py

from db_operations import create_table, drop_table, insert_user, get_users, get_user_by_name

def main():
    # Drop the table if it exists
    drop_table()
    
    # Create the table
    create_table()
    
    # Insert users
    insert_user('Leanne', 111)
    insert_user('Jakes', 45)
    insert_user('Charlie', 35)
    
    # Fetch all users
    print("All users:")
    users = get_users()
    for user in users:
        print(user)
    
    # Fetch user by name
    print("\nUser named Leanne:")
    user = get_user_by_name('Leanne')
    print(user)

if __name__ == '__main__':
    main()
