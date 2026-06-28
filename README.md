# 📚 Bookhub

[![Django](https://img.shields.io/badge/Django-5.1.3-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](https://choosealicense.com/)

**Bookhub** is a premium, robust bookstore and inventory/warehouse management platform built on the Django framework. It provides complete capabilities for organizing books, authors, categories, managing user roles, executing purchases, tracking transaction histories, and operating a dedicated administrative control panel.

---

> [!CAUTION]
> ### 🚫 Proprietary Code & Usage Restriction
> This repository and all its source files are the exclusive property of the author. Copying, distributing, modifying, or using this project for public, commercial, or unauthorized personal purposes is **strictly prohibited**. Failure to comply with these terms may result in account termination, repository removal, or other direct enforcement and recovery actions.

---

## 🌟 Key Features

- 👤 **User Authentication & Management:** Hashed password storage, user login/registration, and authentication middleware.
- 📦 **Inventory & Warehouse Tracking:** Map books to multiple warehouses to track stock locations efficiently.
- 📖 **Catalog Management:** Categorized list of books including author bios, photos, descriptions, and unique system IDs.
- 💳 **Purchase History & Transactions:** Log client purchases, maintain receipt archives, and track quantities.
- 🛠️ **Admin Panel Dashboard:** A dedicated space for administrators to oversee store metrics, manage book databases, and moderate user accounts.

---

## 📁 Repository Structure

```text
Bookhub/
│
├── adminpanel/            # Administrative dashboard and statistics
├── home/                  # Customer landing pages, catalog view, and general views
├── user/                  # Registration, login, profile dashboards, and session controls
├── mysite/                # Core Django project configuration files
│   ├── settings.py        # Django configuration variables
│   ├── urls.py            # Global URL routing
│   └── middleware.py      # Custom middleware (login/logout restrictions)
│
├── media/                 # Dynamic uploaded files (books and author covers)
├── staticfiles/           # Gathered static assets for deployment
├── manage.py              # Django project manager script
├── .gitignore             # Configured git ignore definitions
└── README.md              # Documentation
```

---

## 🛠️ Installation & Setup

Follow these steps to get the environment ready for local development:

### 1. Prerequisites
Make sure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Kokateanand/Bookhub.git
cd Bookhub
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Windows (Command Prompt)
venv\Scripts\activate
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies
Ensure Django and Pillow (for image support) are installed:
```bash
pip install django pillow
```

### 5. Setup Database
Perform database migrations to initialize tables:
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Account)
Create an admin credential to gain access to the admin dashboard:
```bash
python manage.py createsuperuser
```

### 7. Run the Local Server
Start the development server:
```bash
python manage.py runserver
```
Visit the application at `http://127.0.0.1:8000/`.

---

## 🔒 Security Best Practices

To secure this project before deploying to any server:

1. **Secret Key Isolation:**
   In [settings.py](file:///d:/github/Bookhub/mysite/settings.py), the `SECRET_KEY` is currently defined in plain text. For production environment builds, load this from an environment variable:
   ```python
   import os
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-development-key')
   ```

2. **Debug Mode:**
   Ensure `DEBUG = False` is set in production deployment configurations to prevent internal error tracebacks from being shown to users.

3. **Database Security:**
   Do not commit local SQLite databases containing test users or administrator credentials to public version-controlled systems. The `db.sqlite3` file has been added to `.gitignore` to prevent leaks.
