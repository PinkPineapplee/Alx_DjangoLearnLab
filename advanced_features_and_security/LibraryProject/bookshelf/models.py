from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(username, email, password, **extra_fields)



# Custom User Model

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
            ("can_view", "Can view book"),
        ]

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    # REQUIRED EXACT STRINGS: "can_view", "can_create", "can_edit", "can_delete"
    class Meta:
        permissions = [
            ('can_view', 'Can view document'),
            ('can_create', 'Can create document'),
            ('can_edit', 'Can edit document'),
            ('can_delete', 'Can delete document'),
        ]

    def __str__(self):
        return self.title   