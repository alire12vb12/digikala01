from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "PhoneNumber"}),
        required=False
    )
    
    
    address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Address1"}),
        required=False
    )
    
    
    address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Address2"}),
        required=False
    )
    
    
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your City"}),
        required=False
    )
    
    
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your State"}),
        required=False
    )
    
    
    
    zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your PostalCode"}),
        required=False
    )
    
    
    county = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Country;"}),
        required=False
    )
    
    
    class Meta:
       model = Profile
       fields = ("phone", "address1", "address2", "city", "state", "zipcode", "county")




class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "type": "password",
                "placeholder": "Enter password (8 characters)",
            }
        ),
    )

    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "type": "password",
                "placeholder": "Enter password again (8 characters)",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]


# برای پروفایل در هدر
class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your lastname"}
        ),
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )

    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your lastname"}
        ),
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
        ),
    )

    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "type": "password",
                "placeholder": "Enter password (8 characters)",
            }
        ),
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "type": "password",
                "placeholder": "Enter password again (8 characters)",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]
