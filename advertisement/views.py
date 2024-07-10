from django.shortcuts import render

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