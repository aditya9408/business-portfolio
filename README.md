# Carpenter Portfolio Website

A fully responsive, dynamic web application built with Django to showcase the portfolio of a carpenter. The website displays work photos, project details, and includes an integrated contact form powered by email functionality.

---

## ✨ Features

✅ Home page introducing the carpenter’s services  
✅ Portfolio page displaying project images and details  
✅ Contact form that sends emails via SMTP  
✅ Responsive design using Bootstrap  
✅ Typing animations and smooth transitions for enhanced UX  
✅ Environment variables for secure configuration  
✅ Modular and clean code structure

---

## 🚀 Tech Stack

**Frontend:**

- HTML5
- CSS3
- Bootstrap 5
- JavaScript (for animations)

**Backend:**

- Python 3
- Django 4

**Database:**

- SQLite (default for development)

**Environment Management:**

- python-decouple for secure settings

---

## 🔧 Installation & Setup

### 1. Clone the repository:

```bash
git clone https://github.com/aditya9408/vishwakarma-business-site.git
cd vishwakarma-business-site

```
On Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
```
On Linux/macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```

Install Requirments:
```bash
pip install -r requirements.txt
```

## 🔧 Configure environment variables:

SECRET_KEY=your-django-secret-key
DEBUG=True

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=

DEFAULT_FROM_EMAIL=
CONTACT_EMAIL=

Run Migrations
```
python manage.py migrate
```

  Start the development server:
```bash
python manage.py runserver
```

Your Localhost 
```
http://127.0.0.1:8000/
```


