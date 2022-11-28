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
    path('saludar/volver/', views.volver, name='volver'),
    path('saludar/saludando/', views.saludando, name = 'saludando'),
    path('saludar/autoescape/', views.autoescape, name = 'autoescapar'),
    path('saludar/verbatim/', views.verbatim, name = 'verbatim'),
    path('frutas/', views.frutas, name = 'frutas'),
    path('frutas/sacar/<int:id>', views.sacar, name='sacar'),
    path('frutas/suma_fruta/', views.suma_fruta, name = 'suma_fruta'),
    path('frutas/suma_fruta/agregar_fruta/', views.agregar_fruta, name = 'agregar_fruta'),   
    path('testing/', views.testing, name = 'testing'),
    path('testing/volver/', views.volver, name='volver'),
   ]
   