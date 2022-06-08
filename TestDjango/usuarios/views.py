from audioop import reverse
from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView,ListView

from .forms import Formulario
from .models import Usuario
 




from .forms import formulariologin

class Login(FormView):
    template_name='core/iniciosesion.html'
    form_class = formulariologin
    success_url=reverse_lazy("index")
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,** kwargs)
    def form_valid(self,form):
        login(self.request,form.get_user())                               
        return super(Login,self).form_valid(form)
    
def logoutU(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class ListadoUsuario(ListView):
    model=Usuario
    template_name = 'listar_usuario.html'
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)




class crearusuario(CreateView):
    model = Usuario
    form_class= Formulario
    template_name = 'registro.html'
    success_url = reverse_lazy('usuarios:listar_usuario')

