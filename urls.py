"""online_clothing_store URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples: We have used functional viwes in urls for cart
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('add_to_cart', views.add_to_cart, name='add_to_cart')
"""
from django.urls import path
from app import views

urlpatterns = [
    path('registration/',views.CustomerRegistrationView.as_view(), name="customerregistration")
] 
