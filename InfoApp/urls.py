from django.urls import path
from InfoApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]