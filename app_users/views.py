from django.shortcuts import redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app_users.forms import UserSigninForm, UserSignupForm, UserUpdateForm, ProfileForm

from app.abstract.Renderer import Renderer
from app.enums.HttpMethods import HttpMethod

class UsersRenderer(Renderer):
    def signin(self, request) -> HttpResponse:
        form = UserSigninForm(request)

        if request.method == HttpMethod.POST:
            form = UserSigninForm(request, data=request.POST)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("app_contents:home")
                
                form.add_error(None, "Email or Password is incorrect.")

        context: dict = {
            'form': form
        }
        return self.render(request, "users/signin.html", context)

    def signup(self, request) -> HttpResponse:
        form = UserSignupForm()

        if request.method == HttpMethod.POST:
            form = UserSignupForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data.get("username")
                
                form.save()
                messages.success(request, f"Your account has been created. Login in as {username}")

                return redirect("app_users:signin")
            
        context: dict = {
            'form': form
        }

        return self.render(request, "users/signup.html", context)

    def signout(self, request) -> HttpResponse:
        if request.user.is_authenticated:
            logout(request)

        return redirect("app_users:signin")

    def profile(self, request, username: str) -> HttpResponse:
        form1 = UserUpdateForm()
        form2 = ProfileForm()

        context: dict = {
            'form1': form1,
            'form2': form2,
        }
        return self.render(request, "users/user.html", context)

    def delete(self, request, username: str) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/delete.html", context)

    def update(self, request, username: str) -> HttpResponse:
        context: dict = {}
        return self.render(request, "users/update.html", context)
