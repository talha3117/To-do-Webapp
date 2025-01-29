Here’s the updated README with the revised directory structure:

---

# To-Do List Website

This is a simple, yet fully functional To-Do List website built using Django. The website allows users to register, log in, and manage tasks by creating, editing, marking tasks as done, and deleting them. Additionally, users can view a history of completed tasks and filter tasks by their status (completed or not completed).

## Features:
- **User Authentication**: Users can register, log in, and log out.
- **Task Management**: Users can add, edit, mark as done, and delete tasks.
- **Task History**: View a history of tasks, with completed tasks marked accordingly.
- **Filtering**: Filter tasks by their status: All, Completed, or Not Completed.
- **Responsive Design**: The application is responsive, making it accessible on both desktop and mobile devices.

## Technologies Used:
- **Django**: The web framework used for backend logic and routing.
- **SQLite**: The default database engine used to store tasks and user information.
- **HTML/CSS**: The markup and styling technologies used to build and design the pages.
- **Bootstrap** (optional, but may be added for additional styling): Used for responsive design and layout (if desired).
- **JavaScript (optional)**: Can be used for front-end features such as form validation or dynamic interactions.

## Installation Instructions:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/todolist-website.git
   cd todolist-website
   ```

2. **Create and Activate a Virtual Environment**:
   It is recommended to create a virtual environment to isolate your dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run migrations to set up the database schema.
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**:
   If you want to create an admin account to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**:
   Run the server locally to test the project.
   ```bash
   python manage.py runserver
   ```

   Access the site by visiting [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Directory Structure:
```
todo_project/
│
├── tasks/                
│   ├── migrations/       
│   │   ├── admin.py      
│   ├── apps.py          
│   ├── forms.py         
│   ├── models.py        
│   ├── tests.py         
│   ├── urls.py          
│   └── views.py         
│
├── templates/
│   ├── registration/       
│   │   └── login.html         
│   ├── login.html      
│   ├── register.html   
│   ├── task_list.html  
│   ├── add_task.html   
│   └── edit_task.html   
├── todo_list/         
│   ├── __init__.py
│   ├── settings.py       
│   ├── urls.py           
│   ├── wsgi.py           
│   └── asgi.py           
│
├── db.sqlite3            
│
├── manage.py             
```

### Templates:
- **add_task.html**: Form for adding new tasks to the to-do list.
- **edit_task.html**: Form for editing existing tasks.
- **home.html**: Home page with login and registration options.
- **login.html**: Login page for existing users.
- **register.html**: Registration page for new users.
- **task_list.html**: Displays the list of tasks with options to edit, delete, or mark as done.

### Static Files:
- All styles are applied inline within the HTML files, ensuring there are no external CSS files.

## Usage:

- **Homepage**: Upon visiting the homepage, users can either log in or register a new account.
- **Task List**: Once logged in, users can view their tasks, filter by status, and interact with the task list (add, edit, delete, mark as done).
- **Adding a Task**: On the "Add Task" page, users can create a new task and assign it a title.
- **Editing a Task**: Users can edit the title of existing tasks.
- **Marking Tasks as Done**: Users can mark tasks as completed, which will update the task’s status.
- **Task History**: Users can view all tasks (including completed and not completed) through filtering options.

## Screenshots:
### 1. Home Page
![Home Page](screenshots/home.png)

### 2. Login Page
![Login Page](screenshots/login.png)

### 3. Task List Page
![Task List Page](screenshots/task_list.png)

### 4. Add Task Page
![Add Task Page](screenshots/add_task.png)

## Notes:
- This project uses **SQLite** as the database, which is suitable for development and testing. For production environments, it is recommended to configure a more robust database system like PostgreSQL or MySQL.
- The website is designed to be **responsive**, so it should work well on both desktop and mobile devices.
- You may choose to extend the functionality by adding features such as deadlines, task prioritization, or email notifications.

## Contributing:
If you wish to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License:
This project is open-source and available under the MIT License.

---

Let me know if you need any further changes!
