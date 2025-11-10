from django.db import models
from django.utils import timezone

from pathlib import Path
from uuid import uuid4

from app_users.models import User


def post_image_url(instance, filename: str) -> Path:
    ext: str = Path(filename).suffix
    new_filename = f"{instance.user.username}{uuid4().hex}{ext}"

    return Path("images/posts") / new_filename

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=post_image_url)
    posted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-posted_at", "user__username"]
        get_latest_by = ["posted_at"]

    def __str__(self) -> str:
        return f"Post: {self.pk} - {self.user}"
    