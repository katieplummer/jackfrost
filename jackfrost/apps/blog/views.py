from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Article, ArticleImage

# Create your views here.

class BlogListView(ListView):
    model = Article
    template_name = "blog/blog.html"
    context_object_name = "articles"

class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/blog-post.html"
    context_object_name = "article"