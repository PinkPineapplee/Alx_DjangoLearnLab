from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

def user_avatar_path(instance, filename):
    # uploaded to MEDIA_ROOT/avatars/user_<id>/<filename>
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  # oldest first; change to '-created_at' for newest first

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    def get_edit_url(self):
        return reverse('comment-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('comment-delete', kwargs={'pk': self.pk})





