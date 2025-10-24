from django.urls import path

from .views import *

app_name: str = "app_users"

urlpatterns: list = [
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signup"),
    path("signup/", signup, name="signout"),
    path("user/<str:username>", profile, name="profile"),
    path("delete/<str:username>", delete, name="delete"),
    path("update/<str:username>", update, name="update"),
]