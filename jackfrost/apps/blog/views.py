from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Article, ArticleImage

# Create your views here.

def index_view(request):
    return render(request, "index.html")

class BlogListView(ListView):
    model = Article
    template_name = "blog/blog.html"
    context_object_name = "articles"
