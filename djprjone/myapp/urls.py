"""
Author : GOVIND
Date   : 28-01-2025
"""
from django.urls import path
from myapp import views

urlpatterns = [
   path("", views.home_func, name="home"),
   path("http/", views.http_func, name="http"),
]
