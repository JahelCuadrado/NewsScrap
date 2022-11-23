from rest_framework.generics import ListAPIView
from .serializers import PublicoNewsSerializer
from .models import NoticiasPublico
from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
# Create your views here.
   
class PublicoNewsCrud(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PublicoNewsSerializer
    queryset = NoticiasPublico.objects.all().order_by('-id')