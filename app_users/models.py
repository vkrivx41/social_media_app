from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    class Gender(models.TextChoices):
        male = "male", "Male"
        female = "female", "Female"

    gender = models.CharField(max_length=10, choices=Gender.choices)
    date_joined = models.DateField(auto_now=timezone.now)

    def __str__(self):
        return super().__str__()


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="images/profiles/")

    def __str__(self):
        return f"Profile: {self.user.username}"
