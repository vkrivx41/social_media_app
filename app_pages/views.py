from django.shortcuts import render, HttpResponse

from app.abstract.Renderer import Renderer


class PagesRenderer(Renderer):
    def about(self, request) -> HttpResponse:
        return self.render(request, "pages/about.html")
    