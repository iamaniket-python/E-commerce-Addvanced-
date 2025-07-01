from django.db import models
from django.urls import reverse

# Create your models here.

# product caterogry model
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, primary_key=True, unique=True)
    describe=models.TextField(max_length=1000,blank=True,null=True)
    cat_image=models.ImageField(upload_to='category/',blank=True,null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])   

    def __str__(self):
        return self.name