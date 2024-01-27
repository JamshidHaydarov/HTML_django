from django.contrib import admin
from django.urls import path, include
from .views import main_menu

urlpatterns = [
    path('', main_menu),
    ]