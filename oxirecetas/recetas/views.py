from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'recetas/index.html', {})

def premium(request):
    return render(request, 'recetas/premium.html', {})

def Comunidad(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'recetas/Comunidad.html', {'posts': posts })

def registrar(request):
    return render(request, 'recetas/registrar.html', {})

def vegetariana(request):
    return render(request, 'recetas/vegetariana.html', {}) 

def italiana(request):
    return render(request, 'recetas/italiana.html', {})

def chilena(request):
    return render(request, 'recetas/chilena.html', {})

def francesa(request):
    return render(request, 'recetas/francesa.html', {})

def comPremium(request):
    return render(request, 'recetas/comPremium.html', {})
