# Advanced Task Manager

A Flask-based web application for managing tasks with user authentication and a responsive dashboard.

## Features

- ✅ User authentication (signup/login)
- ✅ Create, read, update, and delete tasks
- ✅ Responsive web interface
- ✅ Task management dashboard
- ✅ User session management with Flask-Login

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: SQLite
- **Frontend**: HTML/CSS

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/Sinchu911/advance-clii-task.git
cd advance-clii-task

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
``` 

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
advance-clii-task/
├── app.py              # Main application entry point
├── auth.py             # Authentication logic
├── models.py           # Database models
├── tasks.py            # Task management logic
├── extensions.py       # Flask extensions (db, login_manager)
├── requirements.txt    # Project dependencies
├── base.html           # Base template
├── login.html          # Login page
├── signup.html         # Signup page
├── dashbord.html       # Task dashboard
├── edit_task.html      # Task editing page
└── README.md           # This file
```

## Usage

1. **Sign Up**: Create a new account
2. **Log In**: Sign in with your credentials
3. **Create Tasks**: Add new tasks from the dashboard
4. **Manage Tasks**: Edit or delete existing tasks

## Future Improvements

- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Task priorities
- [ ] Improved UI/UX
- [ ] API endpoints
- [ ] Deployment guide

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.
