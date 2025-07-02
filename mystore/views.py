from django.shortcuts import render
from . models import Product
# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)

    context ={
        'products':products
    }
    return render(request, 'store/store.html',context)


def product_detail(request,category_slug,product_slug):
      

  return render(request,'store/product_detail.html')

