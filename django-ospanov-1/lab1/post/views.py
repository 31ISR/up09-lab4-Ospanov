from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'post/post_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post/post_page.html', {'post': post})