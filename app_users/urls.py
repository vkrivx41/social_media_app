from django.urls import path

from .views import *

app_name: str = "app_users"

renderer: Renderer = UsersRenderer(app_name)

urlpatterns: list = [
    path("signin/", renderer.signin, name="signin"),
    path("signout/", renderer.signout, name="signup"),
    path("signup/", renderer.signup, name="signout"),
    path("user/<str:username>", renderer.profile, name="profile"),
    path("delete/<str:username>", renderer.delete, name="delete"),
    path("update/<str:username>", renderer.update, name="update"),
]