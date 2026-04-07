from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentoForm
from .models import Documento
import os

# Create your views here.

def subir_archivo(request):
    query = request.GET.get('q') 
    
    if query:
        archivos = Documento.objects.filter(titulo__icontains=query).order_by('-subido_el')
    else:
        archivos = Documento.objects.all().order_by('-subido_el')

    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentoForm()

    return render(request, 'index.html', {'form': form, 'archivos': archivos})

def eliminar_archivo(request, archivo_id):
    documento = get_object_or_404(Documento, id=archivo_id)
    documento.delete()
    
    # 3. Redirigimos al index
    return redirect('index')