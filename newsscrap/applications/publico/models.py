from django.db import models

# Create your models here.
class NoticiasPublico(models.Model):  
    titulo       = models.CharField(max_length=200, unique=True)
    descripcion  = models.TextField(blank=True, null=True)
    url          = models.URLField(blank=True, null=True)
    imagen       = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo