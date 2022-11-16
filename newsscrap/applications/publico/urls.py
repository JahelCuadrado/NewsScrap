from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('noticias/publico/', views.PublicoNewsListApiView.as_view()),
]
