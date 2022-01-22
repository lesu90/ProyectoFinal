from django.urls import path
from AppCoder import views


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    
    path("registro/", views.registro, name="registro"),
    
    path("contacto/", views.contacto, name="contacto"),
    
    path("reseñas/", views.reseñas, name="reseñas"),
    
    path("discos/", views.discos, name="discos"),
    
]



