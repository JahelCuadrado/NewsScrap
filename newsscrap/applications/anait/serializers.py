from rest_framework import serializers
from .models import NoticiasAnait

class AnaitNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticiasAnait
        fields = ('__all__')