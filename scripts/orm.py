
from app_users.models import User, Profile


def run():
    user = User.objects.first()
    print(Profile.objects.get_or_create(user=user))