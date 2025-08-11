My Awesome Blog - A Django Blog Project
"My Awesome Blog" is a full-featured blog application built using the Django framework. It provides a clean and modern interface for reading and writing blog posts, complete with user authentication and search features.

Screenshots
Here are some screenshots of the project:

Homepage

![Image description](https://i.postimg.cc/jjjfKGv7/Screenshot-2025-08-11-132405.png)

Blog Post Detail Page
![Image description](https://i.postimg.cc/mDCgGjx9/Screenshot-2025-08-11-134332.png)

New Post Form

Key Features
User Authentication: Users can sign up, log in, and log out.

Post Management (CRUD): Logged-in users can create, read, update, and delete blog posts.

Search Functionality: Users can search for specific posts.

Comment System: Users can leave comments on blog posts.

Image Uploads: Functionality to upload images with posts.

Responsive Design: The website layout is optimized for both desktop and mobile devices.

Technologies Used
Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite 3 (For Development)

Local Setup and Installation
Follow these steps to run this project on your local machine:

Clone the Repository:

git clone [https://github.com/Amangupta87410/my-django-blog.git](https://github.com/Amangupta87410/my-django-blog.git)
cd my-django-blog

Create and activate a virtual environment:

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser to access the admin panel:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Your application will now be running at http://127.0.0.1:8000/.

Project Structure
my-django-blog/
├── blog/                 # Main Django app for blog functionality
├── media/post_images/    # Directory for user-uploaded images
├── myblogsite/           # Django project settings
├── static/css/           # Static files (CSS, etc.)
├── README.md
├── build.sh              # Deployment script
├── db.sqlite3            # SQLite database file
├── manage.py             # Django's command-line utility
└── requirements.txt      # Python dependencies




