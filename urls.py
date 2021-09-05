"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', ProductDetailView.as_view(), name='pre-detail')

"""
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
path('women/', views.women, name='women'),
path('women/<slug:data>', views.women, name='womendata')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)