# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone

# class User(AbstractUser):
#     gender = models.CharField(choices=["Male", "Female"])
#     date_joined = models.DateField(auto_now=timezone.now)
                                   
# class Post(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="images/posts")
                              
# class Profile(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="images/profiles")