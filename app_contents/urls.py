from django.urls import path

from .views import *

app_name: str = "app_contents"

renderer = ContentsRenderer(app_name)

urlpatterns: list = [
    path("", renderer.home, name="home"),
    path("create/", renderer.create, name="create"),
    path("delete/<int:id>", renderer.delete, name="delete"),
    path("update/<int:id>", renderer.update, name="update"),
]