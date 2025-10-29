from django import forms

from app_users.models import User


class UserLoginForm(forms.ModelForm):
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