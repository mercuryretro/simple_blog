from django.shortcuts import render, redirect


# Create your views here.


def landing(request):
    return render(request, "landing.html")


def registration_form(request):
    return render(request, "registration_form.html")
