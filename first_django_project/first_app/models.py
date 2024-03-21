from django.db import models
from django.contrib.auth.models import User
from product.models import product

# Create your models here.
class cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    products=models.ManyToManyField(product,through="CartItem")

class CartItem(models.Model):
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=200,primary_key=True,default="OrderXYZ")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=255,default="abc@email.com")
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    pincode=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False  )

    def __str__(self):
        return f"{self.first_name}-{self.created_at}"

class order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    total=models.IntegerField()
    
