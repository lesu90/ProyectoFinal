

from tkinter.tix import Form
from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import redirect
#from AppCoder.forms import ReseñasForm
from AppCoder.models import reseñas


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def registro(request):
    return render(request, "AppCoder/registro.html")

def contacto(request):
    return render(request, "AppCoder/contacto.html")
    
def discos(request):
    return render(request, "AppCoder/discos.html")

def reseñas(request):
    if request.method == 'POST':
        formulario = reseñas(request.POST["Mensaje"], request.POST["Email"], request.POST["Fecha"])
        formulario.save()
        return render(request, "AppCoder/inicio.html")
    return render(request, 'AppCoder/reseñas.html')


 #'''        if formulario.is_valid():
  #          data = formulario.cleaned_data
   #         reseñas.objects.create(Mensaje=data['Mensaje'], Email=data['Email'])
    #        return redirect('reseñas')
    #else:
    #    formulario = ReseñasForm()
    #return render(request, 'AppCoder/reseñas.html', {'formulario': formulario})

 