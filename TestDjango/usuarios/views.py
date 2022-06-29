
from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.views.generic import CreateView,ListView,TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import Formulario
from .models import Usuario
from .forms import formulariologin
from .mixins import superusuario


class paginaprincipal(LoginRequiredMixin,TemplateView):
    template_name = 'Pagina principal.html'


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


class ListadoUsuario(LoginRequiredMixin,superusuario,ListView):
    model=Usuario
    template_name = 'listar_usuario.html'
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)




def crearusuario(request):
    data ={
        'form':Formulario()
    } 
    if request.method == 'POST':
        formulario = Formulario(data = request.POST)
        if formulario.is_valid():

            formulario.save()
            username=formulario.cleaned_data.get("username")
            password= formulario.cleaned_data.get("password1")
            
            account= authenticate(username=username,password= password)

            login(request,account)
            


            return redirect(to="index")
        else:
            data["form"] = formulario


    return render(request , 'registro.html',data)



class inicioU(LoginRequiredMixin,TemplateView):
    template_name = 'Pagina principal.html'

