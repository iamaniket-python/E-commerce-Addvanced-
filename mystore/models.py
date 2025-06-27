from django.db import models
from product.models import Category
# Create your models here.

class Product(models.Model):
    pro_name=models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, primary_key=True, unique=True)
    description=models.TextField(max_length=1000,blank=True,null=True)
    price = models.FloatField(default=0.0)
    image=models.ImageField(upload_to='product/',blank=True,null=True)
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pro_name
    