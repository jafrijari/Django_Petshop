from django.db import models

from .managers import product_manager
from autoslug import AutoSlugField

class category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=AutoSlugField(populate_from="category_name")

    def __str__(self):
        return self.category_name



class product(models.Model):  #from models import model
    product_name=models.CharField(max_length=100,default="Product Name")
    product_description=models.TextField(default="Product Description")
    product_price=models.IntegerField(default=0)
    product_brand=models.CharField(max_length=50,default="Paws")
    product_picture=models.ImageField(upload_to="images/",default="")#upload to is used to save files to our folder
    jj=models.Manager() #new manager name
    objects=product_manager() #custom manager , this manager only sorts in ascending
    cm=product_manager()
    category=models.ForeignKey(category,on_delete=models.SET_NULL,null=True)
    #1)cascade can delete category even if it still has product in it
    #2)protect doesnt let you delete category ,if category has 1 or more product in it
    #3)set null allows to delete category(includibng product), and then "-"(hifen) is then showed in place of category


    def __str__(self):
        return self.product_name
    
    

