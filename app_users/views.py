from django.shortcuts import render, HttpResponse

from app_users.forms import UserLoginForm

from app.abstract.Renderer import Renderer

class UsersRenderer(Renderer):
    def signin(self, request) -> HttpResponse:
        form = UserLoginForm()

        context: dict = {
            'form': form
        }
        return self.render(request, "users/signin.html", context)

    def signup(self, request) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/signup.html", context)

    def signout(self, request) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/signout.html", context)

    def profile(self, request, username: str) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/user.html", context)

    def delete(self, request, username: str) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/delete.html", context)

    def update(self, request, username: str) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/update.html", context)
