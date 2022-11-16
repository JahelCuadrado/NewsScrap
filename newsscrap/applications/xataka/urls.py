from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('noticias/xataka/', views.XatakaNewsListApiView.as_view()),
]
