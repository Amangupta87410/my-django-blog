My Awesome Blog - A Django Blog Project
This is a full-featured blog application built using the Django framework. This project allows users to create, read, update, and delete blog posts. It also includes user registration and login functionality.

✨ Key Features
User Authentication: Secure registration, login, and logout functionality.

CRUD Operations: Create, Read, Update, and Delete blog posts.

Image Uploads: Functionality to upload images for blog posts.

Post Categories: Organize posts into different categories.

Responsive Design: The website is designed to look great on both desktop and mobile devices.

🛠️ Tech Stack
Backend: Python, Django

Database: SQLite3 (in Development)

Web Server (for local development): Django Development Server

💻 Local Setup and Installation
To run this project on your local machine, follow these steps:

1. Clone the Repository:
git clone https://github.com/Amangupta87410/my-django-blog
cd myblogsite


2. Create and Activate a Virtual Environment:

# For Windows
python -m venv env
.\env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate


3. Install Required Packages:
pip install -r requirements.txt


5. Run Database Migrations:
python manage.py migrate


5. Create a Superuser:
python manage.py createsuperuser

7. Run the Development Server:
python manage.py runserver

Your application will now be available at http://127.0.0.1:8000/.

🚀 Future Goals
Integrate with a cloud storage service like Cloudinary for media files.

Deploy the application to a cloud platform like Render.

Add a commenting system for blog posts.
