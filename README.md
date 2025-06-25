# 🛠️ Blog API with Django REST Framework

A full-featured Blog API built with Django and DRF to practice foundational backend development concepts. Includes user authentication, CRUD operations, and nested endpoints — perfect for anyone learning how to build RESTful APIs.

---

## 🚀 Features

### 🧑‍💻 User Authentication
- `POST /api/register/` – Register a new user (returns token)
- `POST /api/login/` – Login and receive token
- `GET /api/profile/` – Get user profile (requires auth)
- `PUT /api/profile/` – Update email or password

### 📝 Blog Posts
- `GET /api/posts/` – List all blog posts
- `POST /api/posts/` – Create a new post (auth required)
- `GET /api/posts/<id>/` – Retrieve post
- `PUT /api/posts/<id>/` – Update post (auth required)
- `DELETE /api/posts/<id>/` – Delete post (auth required)

### 💬 Comments
- `GET /api/comments/` – List all comments
- `POST /api/comments/` – Add a comment to a post
- `GET /api/posts/<post_id>/comments/` – List comments for a post
- `POST /api/posts/<post_id>/comments/` – Add comment to a specific post

---

## 🔒 Tech Stack & Tools
- Django 5.x
- Django REST Framework
- DRF Token Authentication
- SQLite (can be swapped for PostgreSQL/MySQL)

---

## 📦 Getting Started

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
