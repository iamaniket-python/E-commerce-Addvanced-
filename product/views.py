from django.http import HttpResponse
from django.shortcuts import render
from commerce.product.models import Category
from mystore.models import Product
from django.shortcuts import get_object_or_404
def home(request,category_slug=None):
    categories =None
    products =None


    if category_slug != None:
        categories = get_object_or_404(Category,category_slug=slug)
    products =Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context ={
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'home.html',context)

