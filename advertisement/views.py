from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

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
    return render(request, "logs/eventos.html")

def Login(request):
    return render(request, "logs/login.html")

@login_required
def home(request):
    return render(request, "admin/index.html")