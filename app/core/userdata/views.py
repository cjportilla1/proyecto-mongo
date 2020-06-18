from django.shortcuts import render
from django.utils import timezone
#from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import DatosUser




class DatosUserListView(ListView):
    template_name = 'nosotros.html'
    model = DatosUser
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
       
