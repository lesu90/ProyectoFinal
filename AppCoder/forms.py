
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField

class registroForm(Form):
  nameForm:CharField()
  emailForm:EmailField()
  dateForm:DateField()

#class ReseñasForm(Form):
 #   Mensaje = CharField()
  #  Email = IntegerField() '''

#class ProfesorForm(Form):
    # Con las vistas basadas en clases no hace falta!
 #   nombre = CharField(max_length=30)
  #  apellido = CharField(max_length=30)
   # email = EmailField()
    #profesion = CharField(max_length=30)


    