
# Create your views here.

from django.shortcuts import render,HttpResponse, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self,request,*args,**Rwargs):
        return render(request, self.template_name,{'TituliloIni':'los saluda Sergio','titulo2':'clases de python'})



def contacto(request):
    formContact = ContactForm()


    #Validar que el formulario tenga una peticion post:
    if request.method == "POST":
        #Reconfiguramos formContact con los datos que hemos enviado, es decir rellenamos la plantilla con el formulario
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj', '')
            usuario = request.POST.get('usuario', '')
            correo = request.POST.get('correo', '')
            mensaje = request.POST.get('mensaje', '')

            #Creamos el objeto con las variables del formulario
            email = EmailMessage(
                "RepoDevelopers: tienes un nuevo mensaje de contacto",
                "De: {} <{}>\n\nEscribio:\n\nTipo de Mensaje:{}\n{}".format(usuario,correo, tipomsj ,mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["camilo@hotmail.com"],
                reply_to=[correo]
            )
            #Enviamos el correo:
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                #No se ha enviado el correo
                return redirect(reverse('contacto')+"?fail")

    return render(request,'contactenos.html',{'formulario':formContact})

