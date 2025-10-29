from django.db import models

from app_users.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/posts/")

    def __str__(self) -> str:
        return f"Post: {self.pk} - {self.user}"
    