from django.urls import path

from .views import *

app_name: str = "app_contents"

urlpatterns: list = [
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("delete/<int:id>", delete, name="delete"),
    path("update/<int:id>", update, name="update"),
]