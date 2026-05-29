# Blog Platform

A full-stack blogging platform built using Django and Django REST Framework.

## Features

- User Authentication
- Create/Edit/Delete Posts
- Image Upload
- Comments System
- Like System
- Search Functionality
- Pagination
- REST APIs
- API Authentication
- Responsive Bootstrap UI

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Bootstrap
- Render

## API Endpoints

### Get All Posts
/api/posts/

### Get Single Post
/api/posts/<id>/

### Create Post
POST /api/posts/

## Installation

```bash
git clone <your-github-link>
cd blogplatform
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
