from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name = 'agregar'),
    path('add/agregar_registro/', views.agregar_registro, name = 'agregar_registro'),   
    path('delete/<int:id>', views.delete, name='eliminar'),
    path('update/<int:id>', views.update, name='update'),
]