from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

from pathlib import Path

def profile_image_path(instance, filename: str) -> Path:
    ext: str = Path(filename).suffix  # get the extension (.jpg, .png)
    new_filename = f"{instance.user.username}{ext}"

    return Path("images/profiles/") / new_filename

class User(AbstractUser):
    class Gender(models.TextChoices):
        male = "male", "Male"
        female = "female", "Female"

    gender = models.CharField(max_length=10, choices=Gender.choices)
    date_joined = models.DateField(auto_now=timezone.now)

    def __str__(self):
        return super().__str__()
    
    def clean(self):
        """
        Modify to validate the password length
        """
        if len(self.password) < 6:
            raise ValidationError({
                'password': "Password must be 6 characters or more"
            })
        
        super().clean()


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to=profile_image_path, null=True)

    def __str__(self):
        return f"Profile: {self.user.username}"
