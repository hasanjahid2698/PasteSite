# 📄 Django Pastebin Project

This repository contains the source code for a **Django-based Pastebin** application. The project allows users to create accounts and securely share files. It's designed for efficient file sharing with user authentication and account management.

---

## 🛠️ Project Features

### 🌟 Core Features:
1. **Account-Based Sharing**:
   - Users can register, log in, and manage their accounts.
   - Secure file sharing with user-specific access.

2. **File Management**:
   - Upload and share files with ease.
   - View, download, and delete files.

3. **Access Control**:
   - Private file sharing based on user permissions.
   - Optional file expiration for time-sensitive data.

4. **User-Friendly Interface**:
   - Intuitive design for seamless navigation.
   - Responsive templates for desktop and mobile devices.

5. **Admin Panel**:
   - Full control over users and uploaded files.
   - Manage file permissions and view analytics.

---

## 🛠️ Technologies Used

- **Django Framework**: Backend development.
- **SQLite**: Default database for development.
- **Bootstrap CSS**: Frontend styling and responsive design.
- **JavaScript**: For interactivity.
- **HTML**: For building templates.

---

## 🚀 How to Set Up Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-pastebin.git
   cd django-pastebin
   ```
2. Set up a virtual environment:
   ```bash
      python -m venv env
      source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser (optional for admin panel access):
    ```bash
    python manage.py createsuperuser
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```
7. Open your browser and navigate to:
    ```arduino
    http://127.0.0.1:8000/
    ```

---


