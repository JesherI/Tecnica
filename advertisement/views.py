from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import AnuncioForm

from .models import Anuncio

def HomePage(request):
    return render(request, 'logs/index.html')

def History(request):
    return render(request, "logs/history.html")

def Nosotros(request):
    return render(request, "logs/nosotros.html")

def Acerca(request):
    return render(request, "logs/Acerca.html")

def Mision(request):
    return render(request, "logs/mision.html")

def Valores(request):
    return render(request, "logs/valores.html")

def Talleres(request):
    return render(request, "logs/talleres.html")

def Normas(request):
    return render(request, "logs/normas.html")

def Eventos(request):  
    anuncios = Anuncio.objects.all()
    return render(request, 'logs/eventos.html', {'anuncios': anuncios})

def Login(request):
    return render(request, "logs/login.html")

@login_required
def home(request):
    return render(request, "admin/index.html")

@login_required
def usuarios(request):
    users = User.objects.all()
    return render(request, 'admin/usuarios.html', {'users': users})

# tu_app/views.py
@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Usuario actualizado con éxito.')
        return redirect('Usuarios')
    return render(request, 'admin/edit_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('Usuarios')
    return render(request, 'admin/delete_user.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuario creado con éxito.')
            return redirect('Usuarios')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')
    return render(request, 'admin/create_user.html')

class Error403View(TemplateView):
    template_name = "error/403.html"

class Error404View(TemplateView):
    template_name = "error/404.html"

class Error500View(TemplateView):
    template_name = "error/405.html"

@login_required
def lista_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios/lista_anuncios.html', {'anuncios': anuncios})

@login_required
def detalle_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'anuncios/detalle_anuncio.html', {'anuncio': anuncio})

@login_required
def nuevo_anuncio(request):
    if request.method == "POST":
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save()
            return redirect('detalle_anuncio', pk=anuncio.pk)
    else:
        form = AnuncioForm()
    return render(request, 'anuncios/editar_anuncio.html', {'form': form})

@login_required
def editar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == "POST":
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            anuncio = form.save()
            return redirect('detalle_anuncio', pk=anuncio.pk)
    else:
        form = AnuncioForm(instance=anuncio)
    return render(request, 'anuncios/editar_anuncio.html', {'form': form})

@login_required
def eliminar_anuncio(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == "POST":
        anuncio.delete()
        return redirect('lista_anuncios')
    return render(request, 'anuncios/eliminar_anuncio.html', {'anuncio': anuncio})
