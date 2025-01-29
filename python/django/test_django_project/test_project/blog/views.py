from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post





class PostList(ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "posts"
    ordering = ["-updated"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"



def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/detail.html", {"post": post})
