from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *


app_name: str = "app_users"

renderer: Renderer = UsersRenderer(app_name)

urlpatterns: list = [
    path("signin/", renderer.signin, name="signin"),
    path("signout/", renderer.signout, name="signout"),
    path("signup/", renderer.signup, name="signup"),
    path("profile/", login_required(renderer.profile), name="profile"),
    path("delete/<str:username>", login_required(renderer.delete), name="delete"),
]
