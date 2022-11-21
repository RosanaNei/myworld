from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name = 'agregar'),
    path('add/agregar_registro/', views.agregar_registro, name = 'agregar_registro'),   
    path('delete/<int:id>', views.delete, name='eliminar'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('saludar/', views.saludar, name = 'saludar'),
    path('saludar/saludando/', views.saludando, name = 'saludando'),
    path('saludar/autoescape/', views.autoescape, name = 'autoescapar'),
    path('saludar/verbatim/', views.verbatim, name = 'verbatim'),
   ]
   