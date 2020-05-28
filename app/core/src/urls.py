from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.HomePageView.as_view(), name='index'),
    path('nosotros/',views.nosotrosPageView.as_view(), name='nosotros'),
    path('contactenos/',views.contactenosPageView.as_view(), name='contactenos'),
]