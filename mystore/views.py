from django.shortcuts import render, get_object_or_404
from .models import Product, Category  # adjust based on your models

def store(request, category_slug=None):
    category = None
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    
    try:
        singel_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    

    context ={
        'singel_product':singel_product
    }

    return render(request, 'store/product_detail.html', context)
