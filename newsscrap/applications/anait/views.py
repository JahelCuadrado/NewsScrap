from .serializers import AnaitNewsSerializer
from .models import NoticiasAnait
from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet


class AnaitNewsCrud(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AnaitNewsSerializer
    queryset = NoticiasAnait.objects.all().order_by('-id')