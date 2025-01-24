# Python Task Manager

## Introduction
This project is a Python-based system that allows users to register, log in, and manage their tasks. It is a practical demonstration of handling user data, nested menus, and control flow. The project was developed as part of the RITA Africa Bootcamp.

## Features

### 1. User Authentication
- Register with a username and password.
- Login securely with credentials.
- Update profile details (**Task 1 Contribution**).

### 2. Task Manager
- Add, view, delete, and update tasks (**Task 2 Contribution**).

### 3. Profile Management
- View profile information.
- Change password.

## My Contribution

### Task 1: Profile Update
- Enhanced the dashboard to include an option for updating profile details:
  - **Fields**: Name, Address, Phone Number, and Date of Birth.
  - Added input prompts and validation checks to ensure data integrity.
  - Updated the `view_profile()` function to fetch and display updated details dynamically.

### Task 2: Task Management
- Implemented a task manager that allows users to:
  - **Add Tasks**: Users can create tasks with descriptions.
  - **View Tasks**: Displays all tasks created by the user.
  - **Delete Tasks**: Remove specific tasks by name.
  - **Update Tasks**: Modify existing task descriptions.
- Integrated the task manager into the user dashboard.

## How It Works

### 1. Registration
- New users create an account with a unique username and password.
- Passwords must be at least 6 characters long.

### 2. Login
- Existing users log in using their credentials.
- Upon successful login, users access their dashboard.

### 3. Dashboard
- Navigate through the menu to:
  - Update profile details
  - Manage tasks
  - Change passwords

---

### Example Menu
```plaintext
Welcome to the Dashboard
1. Update Profile Details
2. Manage Tasks
   - Add Task
   - View Tasks
   - Delete Task
   - Update Task
3. Change Password
4. Logout
```

## Technologies Used
- Python (core programming language)
- File-based data storage for user and task data management

## Project Structure
```plaintext
├── main.py         # Main program file
├── README.md       # Project documentation
```

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/davidodediran/User-Authentication-and-Task-Management-System-.git
   ```

2. Navigate to the project directory:
   ```bash
   cd User-Authentication-and-Task-Management
   ```

3. Run the program:
   ```bash
   python3 main.py
   ```

## Future Improvements (I am Working on) 
- Implement database integration for scalable data management.
- Add email verification during registration.
- Enhance task filtering options by priority or deadlines.
- Create a web-based interface using Flask or Django.

## License
This project is licensed under the [MIT License](LICENSE).
