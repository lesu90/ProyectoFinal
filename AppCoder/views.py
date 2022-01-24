from tkinter.tix import Form
from django.shortcuts import render,redirect

from django.http import HttpResponse

from AppCoder.forms import RegistroForm
from AppCoder.models import reseñas,Registro



def inicio(request):
    return render(request, "AppCoder/inicio.html")
#######################################################################################################
##ATENCION##
##VIEW DE JOAQUIN
##VIEW para utilizar con forms.py (no funciona),la funcion de abajo si funciona


def registro(request):
    if request.method == 'POST':
        formularioRegistro=RegistroForm(request.POST)
        if formularioRegistro.is_valid():
            dataRegistro=formularioRegistro.cleaned_data
            Registro.objects.create(nombreRegis=dataRegistro['Nombre'],emailRegis=dataRegistro['Email'],fechaDeNacimientoRegis=dataRegistro['Fecha'])
            return redirect('usuarios')
    else:
        formularioRegistro=RegistroForm()
    return render(request, "AppCoder/registro.html",{'formularioRegistro':formularioRegistro})
#########################################################################################################
""" def registro(request):
    if request.method == 'POST':
        Nombre=request.POST['Nombre']
        Email=request.POST['Email']
        FechaDeNacimiento=request.POST['FechaDeNacimiento']
        print(request.POST)
        print(Registro.objects.all())
        Registro.objects.create(nombreRegis=Nombre,emailRegis=Email,fechaDeNacimientoRegis=FechaDeNacimiento)
        #return render(request, "AppCoder/usuarios.html")
        return redirect('usuarios')
    return render(request, "AppCoder/registro.html") """

###############################################################################################################
def Usuarios(request):
    return render(request, "AppCoder/usuarios.html",{'usuarios':Registro.objects.all()})
    
#def busquedaUsuarios(request):
#    busqueda=f"Usuario es: {request.GET['Nombre']}"
#    return HttpResponse(busqueda)

def busquedaUsuarios(request):
    if request.GET["Email"]:
        email=request.GET["Email"]
        #registro=Registro.objects.filter(emailRegis__icontains=email)
        registro=Registro.objects.filter(emailRegis=email)
        return render(request,"Appcoder/busqueda.html", {"registro":registro,"email":email})

    #busqueda=f"Usuario es: {request.GET['Email']}"
    #return HttpResponse(busqueda)


###############################################################################################################


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

 