from django.shortcuts import render
from .models import Post

# Create your views here.

def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})