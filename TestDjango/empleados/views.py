from django.shortcuts import render,redirect
from .models import Empleados
from .forms import form_Empleados

def ingresar(request):
    if request.method=='GET':
        formulario=form_Empleados()
        contexto={
            'formulario':formulario
        }
    else:
        formulario=Empleados(request.POST, files=request.FILES)
        contexto={
            'formulario':formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('crude')

    return render(request, 'ingresar_e.html', {'formulario':formulario})

def crud(request):
        sugerencia=Empleados.objects.all()
        return render(request, 'ver_e.html', context={'every':sugerencia})

        

def form_mod_sugerencia(request,id):
    sugerencia = Empleados.objects.get(rut=id)

    datos ={
        'form': form_Empleados(instance=sugerencia)
    }
    if request.method == 'POST': 
        formulario = form_Empleados(data=request.POST, instance = sugerencia, files=request.FILES)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('crude')
    return render(request, 'mod_e.html', datos)


def form_del_sugerencia(request,id): 
    sugerencia = Empleados.objects.get(rut=id)
    sugerencia.delete()
    return redirect('crude')
