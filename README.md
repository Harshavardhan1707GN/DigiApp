# DigiApp

DigiApp is a digital transaction management system that allows users to perform secure financial transactions. The application provides a user-friendly interface for signing up, logging in, and managing money transfers.

## Features

- User authentication (Signup & Login)
- Dashboard to view account details
- Secure money transfer functionality
- Responsive web interface using HTML & CSS
- Data storage in JSON (or a database if extended)
- Backend powered by Python

## Technologies Used

- **Backend:** Python
- **Frontend:** HTML, CSS
- **Data Storage:** JSON (or database integration in the future)
- **Version Control:** Git & GitHub

## Project Structure

DigiApp/                # Root directory
│── static/             # Static files (CSS, JS, images)
│   └── style.css       # Stylesheet for the application
│── templates/          # HTML templates for rendering pages
│   ├── base.html       # Base template (common layout)
│   ├── dashboard.html  # Dashboard page
│   ├── login.html      # Login page
│   ├── signup.html     # Signup page
│   ├── transfer.html   # Transfer money page
│── app.py              # Main application file (Flask/Django backend)
│── user_data.json      # JSON file for storing user data (temporary storage)
│── README.md           # Documentation file
│── requirements.txt    # Dependencies and libraries
│── .gitignore          # Files to ignore in Git
