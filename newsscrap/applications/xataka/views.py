from rest_framework.viewsets import ModelViewSet
from .serializers import XatakaNewsSerializer
from .models import NoticiasXataka
from .permissions import IsAdminOrReadOnly
# Create your views here.

 
class XatakaNewsCrud(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = XatakaNewsSerializer
    queryset = NoticiasXataka.objects.all().order_by('-id')