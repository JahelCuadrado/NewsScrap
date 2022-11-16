from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import XatakaNewsSerializer
from .models import NoticiasXataka
# Create your views here.

class XatakaNewsListApiView(ListAPIView): 
    serializer_class = XatakaNewsSerializer  
    def get_queryset(self):
        return NoticiasXataka.objects.all().order_by('-id')