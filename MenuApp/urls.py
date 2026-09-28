from django.urls import path
from MenuApp import views

urlpatterns = [
    path('', views.menu),
]