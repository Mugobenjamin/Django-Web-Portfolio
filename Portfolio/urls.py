from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the home view
    path('contact/', views.contact, name='contact'),  # Define the contact view
]