from django.contrib import admin
from first_app.models import order_item
from first_app.models import Order

#tabular inline
#to display orderitems within orders in admin panel
#to display inline
class OrderItemInline(admin.TabularInline):
    model=order_item


#modeladmin makes this class admin
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]
# Register your models here.

admin.site.register(Order,OrderAdmin)
admin.site.register(order_item)

