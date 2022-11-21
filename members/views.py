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
    mymembers = Members.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponseRedirect(context,reverse('index'))