from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'recetas/index.html', {})

def premium(request):
    return render(request, 'recetas/premium.html', {})

def Comunidad(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'recetas/Comunidad.html', {})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'recetas/post_detail.html', {'post': post}) 

def post_new(request):
    form = PostForm()
    return render(request, 'recetas/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'recetas/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'recetas/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('Comunidad')
    
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
