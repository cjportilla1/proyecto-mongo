
# Create your views here.

from django.shortcuts import render,HttpResponse, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from .forms import ContactForm
# Create your views here.


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self,request,*args,**Rwargs):
        return render(request, self.template_name,{'TituliloIni':'los saluda Sergio','titulo2':'clases de python'})




class nosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get(self,request,*args,**Rwargs):
        return render(request, self.template_name,{'Titulos':'Acerca de nosotros','descripcion':'Somos asi','title_1':'Somos un equipo de trabajo conformado por personas comprometidas pero alegres que desea ver esteproyecto volverse en realidad'})



def contacto(request):
	formContact=ContactForm()

	if request.method=="POST":

		formContact=(ContactForm(data=request.POST))
		if formContact.is_valid():

			tipomsj= request.POST.get('tipomsj','')
			usuario= request.POST.get('usuario','')
			correo= request.POST.get('correo','')
			mensaje= request.POST.get('mensaje','')


		#enviar mensaje o email:
			return redirect(reverse('contacto')+"?ok")



	return render(request,'contactenos.html', {'formulario':formContact}) 