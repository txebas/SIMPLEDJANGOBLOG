from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Libro


# Create your views here.
# blog/views.py


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Mostrar 5 posts por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'blog/libro_list.html', {'libros': libros})

def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'blog/libro_detail.html', {'libro': libro})