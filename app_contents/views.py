from django.shortcuts import render, redirect, HttpResponse

from app.abstract.Renderer import Renderer

class ContentsRenderer(Renderer):
    def home(self, request) -> HttpResponse:
        # redirect from / to posts/
        if request.get_full_path() == "/":
            return redirect(to="app_contents:home")

        return self.render(request, "contents/home.html")

    def create(self, request) -> HttpResponse:
        return self.render(request, "contents/create.html")

    def delete(self, request, id: int) -> HttpResponse:
        return self.render(request, "contents/delete.html")

    def update(self, request, id: int) -> HttpResponse:
        return self.render(request, "contents/update.html")
