from django.db import models

# Create your models here.
class NoticiasAnait(models.Model):  
    titulo       = models.CharField(max_length=200, unique=True)
    descripcion  = models.TextField(blank=True, null=True)
    url          = models.URLField(blank=True, null=True)
    imagen       = models.URLField(blank=True, null=True)