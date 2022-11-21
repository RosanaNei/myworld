from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Members



from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def agregar_registro(request):
  x = request.POST['primo']
  y = request.POST['last']
  member = Members(nombre=x, apellido=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  doppo = request.POST['doppo']
  member = Members.objects.get(id=id)
  member.nombre = first
  member.apellido = doppo
  member.save()
  return HttpResponseRedirect(reverse('index'))

def saludar(request):
  template = loader.get_template('saludar.html')
  context = {
    'nombre': 'Rosana',
  }
  return HttpResponse(template.render(context, request))

def saludando(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('saludar.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))  

def autoescape(request):
  template = loader.get_template('saludar.html')
  context = {
    'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
    'footing': 'Hello &lt;i&gt;my&lt;/i&gt; World!'
  }
  return HttpResponse(template.render(context, request))

def verbatim(request):
  lista = Members.objects.all().values()
  template = loader.get_template('saludar.html')
  context = {
    'lista': lista,
  }
  return HttpResponse(template.render(context, request))  