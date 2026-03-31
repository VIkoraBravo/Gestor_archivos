from django.db import models
# 1. Importamos la herramienta especial desde su propia librería
from cloudinary.models import CloudinaryField

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    
  
    archivo = CloudinaryField('archivo', resource_type='auto')
    
    subido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo