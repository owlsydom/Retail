from django.urls import path

from . import views

urlpatterns = [
    path('', views.volumen, name='volumen'),
    path('volumen/', views.volumen, name='volumen'),
    path('resumen/', views.resumen, name='resumen'),
]