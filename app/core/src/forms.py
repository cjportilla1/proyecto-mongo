from django import forms

# creacion de las clases de formuñlarios pendientes

class contacFom(forms.Form):
    
    tipomsj = forms.CharField(label="tipo de peticion", require=True)
    usuario = forms.CharField(label="Tu nombre", require=True)
    correo = forms.EmailField(label="Correo electronico", require=True)
    mensaje = forms.CharField(label="mensaje", require=True)