from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import PublicoNewsSerializer
from .models import NoticiasPublico
# Create your views here.

class PublicoNewsListApiView(ListAPIView): 
    serializer_class = PublicoNewsSerializer  
    def get_queryset(self):
        return NoticiasPublico.objects.all().order_by('-id')