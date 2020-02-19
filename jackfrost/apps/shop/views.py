from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Product

# Create your views here.

class ShopListView(ListView):
    model = Product
    template_name = "shop/shop.html"
    context_object_name = "products"

def index_view(request):
    return render(request, "shop/shop.html")   


