
# Create your views here.

from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView

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
	return render(request,'contactenos.html')