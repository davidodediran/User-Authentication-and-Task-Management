
"""
Completed Assignment: User Authentication System
Task Summary:
This is an authentication system built with Python, where users can register with a username and password
and later login using their credentials. The program stores the registered users and allows only
valid users to log in, create, delete and update tasks.
"""
# TASK 1:
# Implement the dashboard so users can update their profile details
# The profile details should include Name, Address, Phone number & Date of Birth
#------------------------------------------------------------

# Initialize an empty dictionary to store users
user_database = {}

# Function to register a user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = password
    print("Registration successful!")

# Function to login a user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")

# Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Update Profile Details")
        print("4. View Task Manager")
        print("5. Logout")
        choice = input("Enter your choice (1, 2,3,4 or 5): ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            update_profile(username)
        elif choice=="4":
            task_manager(username)
        elif choice == "5":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")
# Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = new_password
    print("Password updated successfully!")
# View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Your Username is: {username}")
    if username in user_database:
        # Fetch the user's details
        details = user_database.get(username)
        # Check if details is a tuple with exactly 4 elements
        if isinstance(details, tuple) and len(details) == 4:
            name, address, phone_number, dob = details
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Phone Number: {phone_number}")
            print(f"Date of Birth: {dob}")
            # Check if the user has entered their name
            if name:
                print(f"Welcome to your dashboard, {name}!")
            else:
                print("Welcome to your dashboard!")
        else:
            print("Users details not updated")
    else:
        print("User not found in the database.")
# Update Profile Details
def update_profile(username):
    print("\n--- Update Profile Details ---")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    dob = input("Enter your date of birth: ")
    print("Profile details updated successfully!")
    # Updating the user record in the database
    user_database[username] = (name, address, phone_number, dob)
    # Display the updated profile details
    print(f"\n--- Updated Profile ---")
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Date of Birth: {dob}")
    # New Profile Details
    print("Profile details updated successfully!")
#***************************************************************

# TASK 2:
# Implement a task manager dashboard for registered users
# A user should be able to add tasks, view tasks, delete tasks and update tasks
#------------------------------------------------------------
# Initialize an empty dictionary to store tasks
task_db = {}
# Add Task
def add_task(username):
    print("\n--- Add Task ---")
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task_db[task_name] = task_description
    print("Task added successfully!")
# View Tasks
def view_tasks(username):
    print("\n--- View Tasks ---")
    if not task_db:
        print("No tasks available!")
    else:
        for task_name, task_description in task_db.items():
            print(f"Task Name: {task_name}")
            print(f"Task Description: {task_description}")
            print("")
    print("End of tasks.")
# Delete Task
def delete_task(username):
    print("\n--- Delete Task ---")
    task_name = input("Enter the task name to delete: ")
    try:
        task_db.pop(task_name)
        print(f"Task {task_name} deleted successfully!")
    except KeyError:
        print(f"Task {task_name} not found")
# Update Task
def update_task(username):
    print("\n--- Update Task ---")
    task_name = input("Enter the task name to update: ")
    if task_name not in task_db:
        print(f"Task {task_name} not found")
        return
    task_description = input("Enter the new task description: ")
    task_db[task_name] = task_description
    print(f"Task {task_name} updated successfully!")
# Task Manager Dashboard
def task_manager(username):
    while True:
        print(f"\n--- Task Manager: {username} ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Logout")
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            delete_task(username)
        elif choice == "4":
            update_task(username)
        elif choice == "5":
            print(f"Task access closed now, {username}!.")
            break
        else:
            print("Invalid choice! Please try again.")

#***************************************************************
# Run the main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")


