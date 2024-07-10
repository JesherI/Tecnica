from django.urls import path
from . import views

urlpatterns = [
    path('/Historia/', views.History, name='History'),
]
