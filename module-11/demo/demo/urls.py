"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from sampson import views   # import from your app

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]




