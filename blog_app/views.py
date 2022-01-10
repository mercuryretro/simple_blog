from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt
import re


# Create your views here.


def landing(request):
    return render(request, "landing.html")


def registration_form(request):
    return render(request, "registration_form.html")
def register(request): #function for act of registration
    if request.method=="GET":
        return redirect('/')
    else:
        password = request.POST['password']
        confirmed_password = request.POST['confirmed_password']

        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # confirmed_hash = bcrypt.hashpw(
        #     confirmed_password.encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
        request.session['user_id'] = new_user.id

        
        return redirect('/')# actually want to redirect to a new success page for login
