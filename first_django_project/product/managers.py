from django.db import models
from django.db.models.query import QuerySet

class product_manager(models.Manager):
    def get_queryset(self):
        return product_QuerySet(self.model)
        #return super().get_queryset().filter(product_price__gt=500) #change name to description to sort product description coloumn
        #return product_QuerySet(self.model).getWhiskas()
        #return product_QuerySet(self.model).dog_products()
    
    #def sorted(self):
        #return super().get_queryset().order_by('product_name')
    
    #def sorted(self):
        #return super().get_queryset().order_by('product_description')
    
    #def sortByPrice(self):
        #return super().get_queryset().order_by('product_price')
    
    

class product_QuerySet(models.QuerySet):
    def getWhiskas(self):
        return self.filter(product_brand="whiskas")
    
    def dog_products(self):
        return self.filter(product_name__icontains="dog")
    

    
    