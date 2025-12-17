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


## Blog Post CRUD

Endpoints:
- /posts/                 GET  -> list all posts
- /posts/new/             GET/POST -> create (login required)
- /posts/<pk>/            GET  -> detail
- /posts/<pk>/edit/       GET/POST -> update (author-only)
- /posts/<pk>/delete/     POST -> delete (author-only)

Permissions:
- Anyone can read (list & detail).
- Only authenticated users can create posts.
- Only the original author can edit or delete their post.

How author is set:
- The CreateView sets `post.author = request.user` in `form_valid`.

## Comment System

Users can view comments under each blog post.
Authenticated users can add comments.
Only the author of a comment can edit or delete it.

### How to add a comment
- Navigate to a blog post
- Click "Add Comment"
- Submit the form

### How to edit/delete
- Available only to the comment author


## Tagging and Search System

Posts can be assigned multiple tags.
Tags help categorize content and improve discoverability.

### Adding Tags
- While creating or editing a post, add tags separated by commas.

### Viewing by Tag
- Click a tag under a post to view all posts with that tag.

### Search
- Use the search bar to find posts by title, content, or tags.
