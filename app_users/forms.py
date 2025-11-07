from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app_users.models import User, Profile


class UserSigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'placeholder': "Enter your username"
        })

        self.fields["password"].widget.attrs.update({
            'placeholder': "Enter your password"
        })

        self.fields["username"].label = ""
        self.fields["password"].label = ""

class UserSignupForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=User.Gender.choices, label="")
    class Meta:
        model = User
        fields = ("email", "username", "gender", "password")

        widgets: dict = {
            "email": forms.EmailInput(attrs={"placeholder": "Email Address", "required": True}),
            "username": forms.TextInput(attrs={"placeholder": "Unique Username", "required": True}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password", "required": True}),
        }

        labels: dict = {
            "email": "",
            "username": "",
            "gender": "",
            "password": "",
        }

    def save(self, commit=True):
        """
        Modify to hash the password before committing the changes to the DB
        commit: Allow commit or not (True by default)
        """
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


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
