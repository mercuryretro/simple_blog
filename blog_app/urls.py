from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),  # localhost:8000
    path(
        'registration_form/', views.registration_form
    ),  # localhost:8000/registration_form
    
]
