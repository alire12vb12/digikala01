from django.shortcuts import render, redirect
from.models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .forms import SignUpForm


def helloworld(request):
    all_products = Product.objects.all()
    ## return HttpResponse(all_products)
    return render(request,'index.html',{'product':all_products})
# Create your views here.


def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully entered")
            return redirect("home")
        else:
            messages.success(request, "There was a problem logging in")
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("You have successfully logged out😊"))
    return redirect("home")

def signup_user(request):
    form =  SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username = username , password = password1)
            login(request, user)
            messages.success(request, ('your account created'))
            return redirect ("home")
        else:
            messages.success(request, (' مشکلی در ثبت نام وجود دارد '))
            return redirect ("signup")
    else:
        return render (request,'signup.html', {'form' : form})
