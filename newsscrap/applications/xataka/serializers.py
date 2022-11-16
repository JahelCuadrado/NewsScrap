from rest_framework import serializers
from .models import NoticiasXataka

class XatakaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticiasXataka
        fields = ('__all__')