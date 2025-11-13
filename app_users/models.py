from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

from django_cleanup import cleanup

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

    def delete(self):
        """
        Modify to delete the user's profile image if it is not a template
        """
        profile_image_url: str = self.profile.image.url

        # if it doesn't contain the template prefix delete the image and don't save it will be deleted soon
        if "images/templates" not in profile_image_url:
            self.profile.image.delete(save=False)

        return super().delete()

@cleanup.ignore
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to=profile_image_path, null=True)

    def __str__(self):
        return f"Profile: {self.user.username}"
    
    def save(self, *args, **kwargs):
        """
        Check if it's an update and delete the file first then update it
        """
        if not self._state.adding:
            # get the old object, get its file, compare to see if it is not the same file then delete the old
            # if the image is a template then skip the deletion process
            old = Profile.objects.get(pk=self.pk)
            if old.image and old.image != self.image and not "images/templates" in old.image.url:
                old_path = Path(old.image.path)

                if old_path.exists():
                    old_path.unlink()
        
        super().save(*args, **kwargs)
