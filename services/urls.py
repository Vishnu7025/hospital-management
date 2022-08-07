from django import views
from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('services/', views.services,name='services'),
    
]
