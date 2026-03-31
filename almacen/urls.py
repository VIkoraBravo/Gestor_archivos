from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.subir_archivo, name='index'),
    path('eliminar/<int:archivo_id>/', views.eliminar_archivo, name='eliminar_archivo'),
]