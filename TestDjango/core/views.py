from django.shortcuts import render, redirect
from .models import Colab
from .forms import SugerenciasForm

# Create your views here.
def paginaprincipal(request):
    return render(request, 'Pagina principal.html')

def galeria(request):
    return render(request, 'Galeria de fotos.html')

def sugerencias(request):
    if request.method=='GET':
        formulario=SugerenciasForm()
        contexto={
            'formulario':formulario
        }
    else:
        formulario=SugerenciasForm(request.POST, files=request.FILES)
        contexto={
            'formulario':formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('crud')

    return render(request, 'core/Sugerencias.html', {'formulario':formulario})

def crud(request):
    sugerencia=Colab.objects.all()
    return render(request, 'core/crud.html', context={'every':sugerencia})

def form_mod_sugerencia(request,id):
    sugerencia = Colab.objects.get(rut=id)

    datos ={
        'form': SugerenciasForm(instance=sugerencia)
    }
    if request.method == 'POST': 
        formulario = SugerenciasForm(data=request.POST, instance = sugerencia, files=request.FILES)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('crud')
    return render(request, 'core/form_mod_sugerencia.html', datos)


def form_del_sugerencia(request,id):
    sugerencia = Colab.objects.get(rut=id)
    sugerencia.delete()
    return redirect('crud')


def inicio(request):
    return render(request, 'core/Iniciosesion.html')