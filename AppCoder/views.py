

from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def registro(request):
    return render(request, "AppCoder/registro.html")

def contacto(request):
    return render(request, "AppCoder/contacto.html")
    
def reseñas(request):
    return render(request, "AppCoder/reseñas.html")
    
def discos(request):
    return render(request, "AppCoder/discos.html")

