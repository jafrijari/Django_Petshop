from django.shortcuts import render
from django.views.generic.list import ListView
from .models import product,category
from django.views.generic import DetailView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url="/login/"),name="dispatch")
class product_view(ListView):
    model=product
    template_name="products.html"

class ProductDetailView(DetailView):
    model=product
    template_name="product_detail.html"
    context_object_name="prod"

def field_lookup(request):
    #  &=AND OPERATOR
    #  |=OR OPERATOR
    #  ~=NOT OPERATOR

    #AND
    #products=product.objects.all().filter(Q(id=10)& Q(product_name="Name Tags"))
    #products=product.objects.all().filter(Q(product_price__lt="1000")& Q(product_name="Name Tags"))

    #OR
    #products=product.objects.all().filter(Q(id=10) | Q(id=11))
    #products=product.objects.all().filter(Q(product_name__icontains="cat")| Q(product_name__icontains="dog"))

    #NOT
    products=product.objects.all().filter(~Q(id=10) & ~Q(id=15) )
    
    
    #products=product.jj.all() #default project manager
    #products=product.cm.sorted() 
    #products=product.cm.sortByPrice()
    #products=product.cm.all().dog_products() 
    
    #filter func below works like where clause in sql
    #products=product.objects.filter(product_brand="whiskas") #filtering brand
    #products=product.objects.filter(product_name="litter") #filtering by name
    

    #products=product.objects.filter(product_price__lt="600") #lt means less than
    #products=product.objects.filter(product_price__lte="500") #lte=less than equal to
    #products=product.objects.filter(product_price__gt="600") #greater than
    #products=product.objects.filter(product_price__gte="600")#greater than equal to

    #contains works just as "like" clause in sql
    #products=product.objects.filter(product_name__contains="Name Tags") #case sensitive
    #products=product.objects.filter(product_name__icontains="name tags") #case insensistive
    
    #startswith - case sensitive and returns data that start with that name
    #products=product.objects.filter(product_brand__startswith='w')
    #products=product.objects.filter(product_brand__startswith='A')
    #products=product.objects.filter(product_brand__startswith='C') 

    #istartswith -case insensitive
    #products=product.objects.filter(product_brand__istartswith='W')
    #products=product.objects.filter(product_brand__istartswith='a')
    #products=product.objects.filter(product_brand__istartswith='c')

    #endswith
    #products=product.objects.filter(product_name__endswith='s')
    #products=product.objects.filter(product_name__endswith='d')
    #products=product.objects.filter(product_name__endswith='r')

    #iendswith
    #products=product.objects.filter(product_name__iendswith='S')
    #products=product.objects.filter(product_name__iendswith='D')
    #products=product.objects.filter(product_name__iendswith='R')

    #in operator
    #products=product.objects.filter(id__in=[10,11,12])
    #products=product.objects.filter(id__in=[10,11])
    #products=product.objects.filter(id__in=[10]) 
    #products=product.objects.filter(product_description__in="healthy")
    #above line returns products with specified ID










    return render(request,"productlookup.html",{"product":products})
    
class category_deatail_view(DetailView):
    model=category
    template_name="category.html"
    context_object_name="category"
    slug_field="slug"
    


    
