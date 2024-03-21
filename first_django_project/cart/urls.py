from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("add-to-cart/<int:productID>",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.view_cart,name="viewcart"),
    path("cart/update/<int:cartItemID>",views.update_cart,name="updatecart"),
    path("cart/delete/<int:cartItemID>",views.delete_cart,name="deletecartItem"),
    path("checkout/",views.check_out,name="checkout"),
    path("payment/<str:orderID>",views.make_payment,name="payment"),
    path("success/<str:order_id>",views.success,name="success"),
    path("fail/<str:order_id>",views.success,name="fail")


]