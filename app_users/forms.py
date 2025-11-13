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

    def clean_username(self):
        """
        Validate the username to be 3 chars or more
        """
        username = self.cleaned_data.get("username")

        if len(username) < 3:
            raise forms.ValidationError(message="Username needs to be 3 characters or more")
        
        return username
    
    def clean_password(self):
        """
        Validate the password's length to be 6 chars or more
        """
        password: str = self.cleaned_data.get("password")

        if len(password) < 6:
            raise forms.ValidationError(message="Password must be 6 characters or more")
        
        return password

    def save(self, commit=True):
        """
        Modify to hash the password before committing the changes to the DB
        commit: Allow commit or not (True by default)
        returns: A user object with a hassed password
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
        fields = ("first_name", "last_name", "email", "gender")

        widgets: dict = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name", "required": True}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name", "required": True}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address", "required": True}),
        }

        labels: dict = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "gender": "",
        }

    def clean_first_name(self):
        """ Validate the first_name to be 2 chars or more """
        first_name = self.cleaned_data.get("first_name")

        if len(first_name) < 2:
            raise forms.ValidationError(message="First name must be 2 or more character")
        
        return first_name
    
    def clean_last_name(self):
        """ Validate the last_name to be 2 chars or more """
        last_name = self.cleaned_data.get("last_name")

        if len(last_name) < 2:
            raise forms.ValidationError(message="Last name must be 2 or more character")
        
        return last_name
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image",)

        widgets: dict = {
            "image": forms.FileInput(attrs={"hidden": True})
        }

        labels: dict = {
            "image": "",
        }
