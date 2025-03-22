# Library-Management-Project 
Folder Structure
LibraryManagement/
│── books/                  # Django app for book management
│   │── migrations/         # Database migrations
│   │── __init__.py         
│   │── admin.py           
│   │── apps.py            
│   │── models.py          # Book model definition
│   │── serializers.py     # DRF serializers
│   │── testapi.py         # API testing script
│   │── tests.py           
│   │── views.py           # API views
│   │── urls.py            # URL routes for book management
│
│── LibraryManagement/      # Project settings
│   │── __init__.py
│   │── settings.py        # Project settings (MySQL configuration, JWT setup)
│   │── urls.py            # Main URL configuration
│   │── wsgi.py           
│   │── asgi.py           
│
│── manage.py              # Django management script
│── requirements.txt       # Dependencies for the project
│── README.md              # Documentation
│── steps.txt              # Any extra notes or steps





This is a Django-based Library Management System that allows admins to manage book records through a RESTful API. Students can view available books.

## Features
- Admin Signup & Login (Token-based authentication)
- CRUD operations for books (Create, Read, Update, Delete)
- JWT Authentication for secure access
- REST API built with Django REST Framework (DRF)
- MySQL database for persistent storage


## Test API Endpoints
Use Postman or testapi.py to test the APIs.

POST /register/ → Register an admin

POST /login/ → Login and get JWT tokens

#Books Management

GET /api/books/ → Get list of all books

POST /books/create/ → Add a new book (Admin only)

PUT /books/update/<book_id>/ → Update book details (Admin only)

DELETE /books/delete/<book_id>/ → Delete a book (Admin only)

## To run Project
python manage.py runserver
