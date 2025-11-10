from django.utils import timezone

from app_users.models import User, Profile
from app_contents.models import Post


def run():
    users = User.objects.all()
    posts = Post.objects.all().order_by("-posted_at")

    posts.update(posted_at=timezone.now())
    # for user in users:
    #     profile, _ = Profile.objects.get_or_create(user=user)
        
    #     if user.gender == User.Gender.male:
    #         profile.image = "images/templates/profile_male.png"
    #     else:
    #         profile.image = "images/templates/profile_female.png"
        
        # profile.save()