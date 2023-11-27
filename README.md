# club_management_system
The Club Management System is a Django-powered web application designed to streamline administrative tasks for clubs. With a focus on user-friendly interfaces and robust functionality, this system provides an integrated platform for managing members, organizing events, and generating reports.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python (version 3.x)
- Django (version 3.x)
- Other dependencies (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dawit-P/club_management_system.git

2. **Navigate to the project directory:**
    ```bash
    cd club_management_system

3. **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv

4. **Activate the virtual environment:**

On Windows:
    ```bash
    venv\Scripts\activate
On macOS and Linux:
    ```bash
    source venv/bin/activate

5. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt


## Email Configuration
To enable email functionality in your Django project, configure the email settings in the settings.py file. Follow the steps below to set up your email backend:

## SMTP Configuration
Open the settings.py file in your Django project.

Locate the section related to email configuration.

**Update the following variables with your SMTP server information:**
    ```bash
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'your_smtp_host'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your_email@example.com'
    EMAIL_HOST_PASSWORD = 'your_email_password'

## Using a Different Email Backend
If you prefer to use a different email backend or service, modify the EMAIL_BACKEND variable accordingly. For example, you can use the console backend for development:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

This will print emails to the console during development, making it easy to debug without sending actual emails.

Running the Application
Now that you have set up the project and configured the email settings, you can run the application:
python manage.py runserver
Visit http://localhost:8000/ in your web browser to access the Club Management System.