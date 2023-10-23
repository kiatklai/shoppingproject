from django.shortcuts import render
from productapp.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
  products=Product.objects.filter(isTrending=True)
  return render(request,"index.html",{"products":products})

def productDetail(request,id):
  product=Product.objects.get(pk=id)
  return render(request,"detail.html",{"product":product})

def products(request):
  all_products=Product.objects.all()
  #pageの番号を設定
  page = request.GET.get("page")
  paginator=Paginator(all_products,3) #1 pageにいくらの商品を表示させるか
  all_products=paginator.get_page(page)
  return render(request,"products.html",{"all_products":all_products})