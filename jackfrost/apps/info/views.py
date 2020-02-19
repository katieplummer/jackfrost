from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def info_view(request):
    return render(request, "info/info.html")
