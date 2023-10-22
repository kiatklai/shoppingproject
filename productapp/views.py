from django.shortcuts import render
from productapp.models import Product

# Create your views here.
def index(request):
  products=Product.objects.filter(isTrending=True)
  return render(request,"index.html",{"products":products})