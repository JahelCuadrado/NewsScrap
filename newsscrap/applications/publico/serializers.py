from rest_framework import serializers
from .models import NoticiasPublico

class PublicoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticiasPublico
        fields = ('__all__')