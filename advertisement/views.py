from django.shortcuts import render

def HomePage(request):
    return render(request, 'logs/index.html')

def AboutPage(request):
    pass