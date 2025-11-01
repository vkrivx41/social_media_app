from django import forms

from app_users.models import User, Profile


class UserSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")

        widgets: dict = {
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }

        labels: dict = {
            "email": "",
            "password": "",
        }


class UserSignupForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=User.Gender.choices, label="")
    class Meta:
        model = User
        fields = ("email", "username", "gender", "password")

        widgets: dict = {
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
            "username": forms.TextInput(attrs={"placeholder": "Unique Username"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }

        labels: dict = {
            "email": "",
            "username": "",
            "gender": "",
            "password": "",
        }


class UserUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=User.Gender.choices, label="")
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "gender", "password")

        widgets: dict = {
            "first_name": forms.EmailInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.EmailInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }

        labels: dict = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "gender": "",
            "password": "",
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image",)

        labels: dict = {
            "image": "",
        }
