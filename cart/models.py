from django.db import models
from mystore.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id =models.CharField(max_length=250,blank=True)
    date_added =models.DateField(auto_now_add=True)


    def __str__(Self):
        return Self.cart_id
    

class CartItem(models.Model):
    product =models.ForeignKey('mystore.Product', on_delete=models.CASCADE)
    cart =models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity =models.IntegerField()
    is_active =models.BooleanField(default=True)

    def sub_total(self):
        return self.product