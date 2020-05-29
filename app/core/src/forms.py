from django import forms

# creacion de las clases de formuñlarios pendientes



class ContacForm(forms.Form):
    tipomsj = forms.CharField(label="tipo de peticion", required=True)
    usuario = forms.CharField(label="Tu nombre", required=True)
    correo = forms.EmailField(label="Correo electronico", required=True)
    mensaje = forms.CharField(label="mensaje", required=True)