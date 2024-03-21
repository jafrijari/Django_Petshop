from django.test import TestCase
from razorpay import Product

# Create your tests here.

from .models import product

class ProductTest(TestCase):
    def setUp(self):
        self.product = product.jj.create(product_name="TestProduct",
                          product_description="TestDescription",
                          product_price=1000,
                          product_brand="TestBrand",
                          product_picture="TestPicture",

                          )
        
    def test_create_product(self):
        Product = product.jj.get(product_name="TestProduct")
        self.assertEqual(Product.id,self.product.id)

    def test_update_product(self):
        Product = product.jj.get(product_name="TestProduct")
        Product.product_price=5000
        Product.save()
        self.assertNotEqual(Product.product_price,self.product.product_price)

    def test_fetch_product(self): 
        Products=product.jj.all()
        count=len(Products)
        self.assertGreater(count,0)

    

    


