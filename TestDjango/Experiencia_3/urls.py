"""Experiencia_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from core.views import paginaprincipal
from django.contrib.auth.views import LoginView,logout_then_login

'''from usuarios.views import Login,logoutU'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginas/', include('core.urls')),
    path('',login_required(paginaprincipal),name="index"),
    path('accounts/login/',LoginView.as_view(template_name='core/iniciosesion.html'),name='login'),
    path('logout',login_required(logout_then_login),name='logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


    '''
    path('accounts/login/',Login.as_view(),name='login'),
    path('logout',login_required(logoutU),name='logout')'''