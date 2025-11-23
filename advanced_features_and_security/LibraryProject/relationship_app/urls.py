from django.urls import path, include
from . import views
from .views import list_books, login_view, logout_view, register_view

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('relationship_app/', include('relationship_app.urls', namespace='relationship_app')),
    path('register/', views.register, name='register'),  # <-- contains "views.register"
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path("add_book/", views.add_book, name="add_book"),          # contains "add_book/"
    path("edit_book/<int:pk>/", views.edit_book, name="edit_book"),  # contains "edit_book/"
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
    path("documents/<int:pk>/view/", views.view_document, name="view_document"),
    path("documents/create/", views.create_document, name="create_document"),
    path("documents/<int:pk>/edit/", views.edit_document, name="edit_document"),
    path("documents/<int:pk>/delete/", views.delete_document, name="delete_document"),

]
