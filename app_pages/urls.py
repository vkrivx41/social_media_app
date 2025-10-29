from django.urls import path
from .views import *

app_name: str = "app_pages"

renderer: Renderer = PagesRenderer(app_name)

urlpatterns: list = [
    path("about/", renderer.about, name="about")
]
