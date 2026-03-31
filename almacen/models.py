from django.db import models

# Create your models here.

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='mis_archivos/') # Se guardarán en /media/mis_archivos/
    subido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo