from django.urls import path
from .views import *

app_name: str = "app_pages"

urlpatterns: list = [
    path("about/", about, name="about")
]
