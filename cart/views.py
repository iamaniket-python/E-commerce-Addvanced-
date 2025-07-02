from django.shortcuts import redirect, render
from.models import *
from mystore.models import Product

# Create your views here.

def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product =Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item =Cart.items.objects.get(product=product,cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except cart_item.DoesNotExist:
        cart_item=cart_item.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart')


def cart(request):

    return render(request, 'store/cart.html')