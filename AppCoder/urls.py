from django.urls import path
from AppCoder import views


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    
    path("registro/", views.registro, name="registro"),
    
    path("usuarios/", views.Usuarios, name="usuarios"),
    
    path("buscar/", views.busquedaUsuarios, name="buscar"),
    
    path("contacto/", views.contacto, name="contacto"),
    
    path("reseñas/", views.reseñas, name="reseñas"),
    
    path("discos/", views.discos, name="discos"),
    
]



