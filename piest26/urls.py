"""
URL configuration for piest26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from advertisement import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='Home'),
    path('Historia/', views.History, name='Historia'),
    path('Nosotros/', views.Nosotros, name='Nosotros'),
    path('Acerca/', views.Acerca, name='Acerca'),
    path('Mision/', views.Mision, name='Mision'),
    path('Valores/', views.Valores, name='Valores'),
    path('Talleres/', views.Talleres, name='Talleres'),
    path('Normas/', views.Normas, name='Normas'),
    path('Eventos/', views.Eventos, name='Eventos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.home, name='Inicio'),
    path('index/',views.home, name='Index'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('usuarios/', views.usuarios, name="Usuarios")
]
