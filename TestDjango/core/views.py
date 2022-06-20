from django.shortcuts import render, redirect
from .models import Colab

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import superusuario

from .forms import SugerenciasForm

from .models import Colab

from .carrito import Carrito



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
    return render(request,'core/Iniciosesion.html')







#carrito en si

def tienda(request):
    
    productos = Colab.objects.all()
    return render(request, "core/tienda.html", {'productos':productos})

def agregarProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Colab.objects.get(productoid=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

    
def eliminarProducto(request,producto_id):
    carrito = Carrito(request)
    producto = Colab.objects.get(productoid=producto_id)
    carrito.eliminar( producto)
    return redirect('carrito')

def restarProducto(request,producto_id):
    carrito = Carrito(request)
    producto = Colab.objects.get(productoid=producto_id)
    carrito.restar( producto)
    return redirect('carrito')

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')


def catalogo(request):
    sugerencia=Colab.objects.all()
    return render(request, 'core/catalogo.html', context={'every':sugerencia})




