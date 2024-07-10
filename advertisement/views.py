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