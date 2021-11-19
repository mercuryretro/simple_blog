from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),  # localhost:8000
]
