# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(
#         label="",
#         max_length=50,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'})
#     )

#     last_name = forms.CharField(
#         label="",
#         max_length=50,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lastname'})
#     )

#     email = forms.EmailField(
#         label="",
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'})
#     )

#     username = forms.CharField(
#         label="",
#         max_length=20,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'})
#     )


#     password1 = forms.CharField(
#        label="",
#        widget=forms.PasswordInput( 
#           attrs={
#             'class':'form-control',
#             'name':'password',
#             'type':'password',
#             'placeholder':'enter password 8 charecter'
#         }
#     )
# )
       

#      password2 = forms.CharField(
#         label="",
#         widget=forms.PasswordInput(  
#             attrs={
#                 'class':'form-control',
#                 'name':'password',
#                 'type':'password',
#                 'placeholder':'enter  again password 8 charecter'
#         }
#     )    
# )
      
# class Meta:
#    model =  User
#    fields = ('first_name','last_name','email','username','password1','password2')

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your lastname'})
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'Enter password (8 characters)'
            }
        )
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'Enter password again (8 characters)'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
