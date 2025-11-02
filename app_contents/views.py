from django.shortcuts import render, redirect, HttpResponse

from app.abstract.Renderer import Renderer

class ContentsRenderer(Renderer):
    def home(self, request) -> HttpResponse:
        # redirect from / to posts/
        if request.get_full_path() == "/":
            return redirect(to="app_contents:home")

        images: list = ["image1.jpg", "image2.jpg", "image3.png", "image4.jpg", "image5.jpg"]

        context: dict = {
            'images': images
        }
        return self.render(request, "contents/home.html", context)

    def create(self, request) -> HttpResponse:
        return self.render(request, "contents/create.html")

    def delete(self, request, id: int) -> HttpResponse:
        return self.render(request, "contents/delete.html")

    def update(self, request, id: int) -> HttpResponse:
        return self.render(request, "contents/update.html")
