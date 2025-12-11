## Authentication System (Registration, Login, Profile)

### Features
- User registration with unique email
- Login / logout using Django auth
- Profile page to edit email, bio, and avatar
- CSRF protection and Django password hashing

### Setup
1. Ensure `Pillow` is installed for image uploads:
   pip install Pillow
2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
3. Create a superuser (optional):
   python manage.py createsuperuser
4. Run the server:
   python manage.py runserver

### Endpoints
- /register/  — create account
- /login/     — login
- /logout/    — logout
- /profile/   — view and edit profile (login required)

### Testing
- Use the included unit tests: `python manage.py test`
- Manual test steps: register, login, edit profile, logout