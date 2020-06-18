from django.urls import path
from .views import DatosUserListView




urlpatterns = [ 
    
    path('nosotros/', DatosUserListView.as_view(), name='nosotros'),
    
]