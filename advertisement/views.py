from django.shortcuts import render

def HomePage(request):
    return render(request, 'logs/index.html')

def History(request):
    return render(request, "logs/history.html")

def Nosotros(request):
    return render(request, "logs/nosotros.html")