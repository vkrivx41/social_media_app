
from app_users.models import User


def run():
    print(User.objects.all())