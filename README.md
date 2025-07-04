# 🛒 E-commerce-Advanced

A powerful, full-featured Django-based e-commerce platform designed for advanced functionality, clean architecture, and scalability. This project showcases key features required in a modern online shopping application, including dynamic cart management, product filtering, authentication, and media handling.

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Add to Cart / Remove from Cart
- ✅ Dynamic Cart Count
- ✅ Category-based Product Filtering with Slugs
- ✅ Product Availability & Stock Control
- ✅ Admin Panel for Managing Products & Categories
- ✅ Image Uploads via Django `ImageField`
- ✅ SEO-friendly URLs
- ✅ Bootstrap for Responsive UI

---

## 🛠️ Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Backend      | Django         |
| Frontend     | HTML, CSS, Bootstrap |
| Database     | SQLite (default) / PostgreSQL |
| Media Files  | Django ImageField |
| Auth System  | Django Auth    |

---

## 📁 Project Structure

E-commerce-Advanced/
├── commerce/ # Django project settings
├── product/ # Product app (models, views, urls)
├── mystore/ # Store/cart logic
├── templates/ # HTML templates
├── media/ # Uploaded product images
├── static/ # CSS/JS/images
├── db.sqlite3 # Default database
└── manage.py


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/E-commerce-Advanced.git
cd E-commerce-Advanced

python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

✅ TODOs / Future Features
Payment Integration (Razorpay/Stripe)

Order History & Invoice

Product Reviews & Ratings

Wishlist Functionality

Email Notifications
