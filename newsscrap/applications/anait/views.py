from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AnaitNewsSerializer
from .models import NoticiasAnait


# Create your views here.
class AnaitNewsListApiView(ListAPIView): 
    serializer_class = AnaitNewsSerializer
    def get_queryset(self):
        return NoticiasAnait.objects.all().order_by('-id')