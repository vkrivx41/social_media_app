from django.shortcuts import redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app_users.forms import UserSigninForm, UserSignupForm, UserUpdateForm, ProfileForm

from app_users.models import User, Profile

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

    def profile(self, request) -> HttpResponse:
        user: User = request.user
        self.get_or_create_profile(user)

        form1 = UserUpdateForm(prefix="credential", instance=request.user)
        form2 = ProfileForm(prefix="profile", instance=request.user.profile)

        if request.method == HttpMethod.POST:
            form1 = UserUpdateForm(request.POST, prefix="credential", instance=request.user)
            form2 = ProfileForm(request.POST, request.FILES, prefix="profile", instance=request.user.profile)

            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                messages.success(request, "Profile updated successfully!")
                return redirect("app_users:profile")
            else:
                messages.error(request, "Please correct the errors below.")

        context = {
            'form1': form1,
            'form2': form2,
            'user': user
        }
        return self.render(request, "users/profile.html", context)

    def delete(self, request, username: str) -> HttpResponse:
        perform_confirmation = request.GET.get("perform") == "1"
        user = request.user
        
        previous_page_url: str = request.META.get("HTTP_REFERER")
        current_page_url: str = request.path

        if previous_page_url is None:
            return redirect("app_users:profile")
        
        if perform_confirmation:
            request.user.delete()
            return redirect("app_contents:home")

        context: dict = {
            'user': user,
            'previous': previous_page_url,
            'current_url': current_page_url,
        }

        return self.render(request, "users/delete.html", context)

    @staticmethod
    def get_or_create_profile(user: User) -> Profile:
        profile, _ = Profile.objects.get_or_create(user=user)
        return profile      
        