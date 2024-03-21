from django.contrib import admin
from .models import product,category


@admin.register(product)
class product_admin(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_price','product_brand','category')

#admin.site.register(product,product_admin)
# Register your models here.

#register category
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')