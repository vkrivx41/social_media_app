from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name: str = "app_contents"

renderer = ContentsRenderer(app_name)

urlpatterns: list = [
    path("", renderer.home, name="home"),
    path("create/", login_required(renderer.create), name="create"),
    path("delete/<int:id>", login_required(renderer.delete), name="delete"),
    path("update/<int:id>", login_required(renderer.update), name="update"),
]
