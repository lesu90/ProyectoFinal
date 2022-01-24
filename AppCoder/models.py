from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model

from django.utils import timezone

from django.db.models.fields import (
    BooleanField, CharField, DateField, EmailField, IntegerField,
    GenericIPAddressField, URLField, DecimalField, TimeField
)
###Lo hizo Jesus
class reseñas(models.Model):
    Mensaje = models.CharField(max_length=300)
    Email = models.EmailField(max_length=300)
    Fecha = models.DateTimeField("date logged") 
    #def __str__(self):
#        """Returns a string representation of a message."""
 #       date = timezone.localtime(self.log_date)
  #      return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
  
  
###Lo hizo Joaquin
class Registro(models.Model):
    nombreRegis = models.CharField(max_length=300)
    emailRegis = models.EmailField(max_length=300)
    fechaDeNacimientoRegis = models.DateField() 

    
    
    