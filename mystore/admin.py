from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name','slug','description','image','stock','is_available','category','created_at','updated_at')
    prepopulated_fields = {'slug':('pro_name',)}

admin.site.register(Product)