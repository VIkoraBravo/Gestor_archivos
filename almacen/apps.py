from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AlmacenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'almacen'

    def ready(self):
        # Conectamos una función que se ejecute justo después de las migraciones
        post_migrate.connect(create_admin, sender=self)

def create_admin(sender, **kwargs):
    from django.contrib.auth.models import User
    import os
    
    # Creamos un superusuario por defecto si no existe ninguno
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@ejemplo.com', 'admin1234')
        print("Superusuario 'admin' creado exitosamente con clave 'admin1234'")