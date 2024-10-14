from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def blog_list(request):
    all_posts = Post.objects.all()

    return render(request, "blog/list.html", {"posts": all_posts})


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/detail.html",  {"post": post})
    
