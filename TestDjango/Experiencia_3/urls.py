from django.contrib import admin

from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


from usuarios.views import Login,logoutU,paginaprincipal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginas/', include('core.urls')),
    path('usuarios/',include('usuarios.urls')), 
    path('',paginaprincipal.as_view(),name="index"),
    path('accounts/login/',Login.as_view(),name='login'),
    path('logout',login_required(logoutU),name='logout'),
    path('empleados/', include('empleados.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


