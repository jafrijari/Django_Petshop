import stat
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,HttpResponse
from product.models import product
from first_app.models import cart,CartItem, order_item
from first_app.models import cart
from .forms import order_form
from first_app.models import Order
import uuid
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def add_to_cart(request,productID):
    products=get_object_or_404(product,id=productID)
    print(products.product_name)
    currentUser=request.user
    carts,created=cart.objects.get_or_create(user=currentUser)
    print(created)
    item,item_created=CartItem.objects.get_or_create(cart=carts,products=products)

    quantity=request.GET.get("quantity")

    if not item_created:
        item.quantity+=int(quantity)
    else:
        item.quantity=1
    item.save() #for saving item in database
    return HttpResponseRedirect("/product/productlookup/")
#===================================================================
#view cart
#===================================================================

def view_cart(request):
    currentUser=request.user
    carts,created=cart.objects.get_or_create(user=currentUser)
    CartItems=carts.cartitem_set.all()
    print(CartItems)
    finalAmount=0

    for item in CartItems:
        finalAmount+=item.quantity*item.products.product_price

    return render(request,"cart.html",{"items":CartItems,"finalAmount":finalAmount})

#===================================================================
#                        UPDATE CART
#===================================================================


def update_cart(request,cartItemID):
    cart_item=get_object_or_404(CartItem,pk=cartItemID)
    quantity=request.GET.get("quantity")
    cart_item.quantity=int(quantity)
    cart_item.save()
    return HttpResponseRedirect("/cart/")


#===================================================================
#                        DELETE CART
#===================================================================

def delete_cart(request,cartItemID):
    
    cart_item=get_object_or_404(CartItem,pk=cartItemID)
    cart_item.delete()
    return HttpResponseRedirect("/cart/")


#================Checkout======

def check_out(request):
    currentUser=request.user
    initial={
        "user":currentUser.get_username(),
        "first_name":currentUser.get_short_name(),
        "last_name":currentUser.last_name,
        "email":currentUser.email
    }


    form=order_form(initial=initial)
    currentUser=request.user
    carts,created=cart.objects.get_or_create(user=currentUser)
    CartItems=carts.cartitem_set.all()
    print(CartItems)
    finalAmount=0

    for item in CartItems:
        finalAmount+=item.quantity*item.products.product_price

    if request.method=="POST":
        form=order_form(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user=request.user
            firstname=form.cleaned_data['first_name']
            lastname=form.cleaned_data['last_name']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            phoneno=form.cleaned_data['phone_no']
            pincode=form.cleaned_data['pincode']
            orderId=str(uuid.uuid4())

            
            order=Order.objects.create(user=user,first_name=firstname,last_name=lastname,address=address,city=city,state=state,pincode=pincode,phone_no=phoneno,
                                 order_id=orderId[0:8])
            
            for item in CartItems:
                order_item.objects.create(
                        order=order,
                        products=item.products,
                        quantity=item.quantity,
                        total=item.quantity*item.products.product_price
                )

            
            
            return HttpResponseRedirect("/payment/"+orderId[0:8])
        else:
            print(form.errors)


        
    

    return render(request,"checkout.html",{"form":form,"items":CartItems,"finalAmount":finalAmount})


#===================================================================
#                        Make payment
#===================================================================
import razorpay


def make_payment(request,orderID):
    #print(orderID)
    order=Order.objects.get(pk=orderID)
    orderItems=order.order_item_set.all()
    amount=0
    for item in orderItems:
        amount+=item.total
    print(amount)

    
    client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))

    data = { "amount": amount*100, "currency": "INR", "receipt": orderID,"payment_capture":1}
    payment = client.order.create(data=data)



    return render(request,"payment.html",{"payment":payment})


#===================================================================
#                        success page
#===================================================================
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail #for mail

@csrf_exempt
def success(request,order_id):
    if request.method=="POST":
        client = razorpay.Client(auth=("rzp_test_f0iQz7zWmSBLiq", "R6sxtB0E6UijcZWfOSWgmhgA"))
        check=client.utility.verify_payment_signature({
            'razorpay_order_id': request.POST.get("razorpay_order_id"),
            'razorpay_payment_id':request.POST.get("razorpay_payment_id"),
            'razorpay_signature': request.POST.get("razorpay_signature")
                    
                    
   })
        if check:
            order=Order.objects.get(order_id=order_id)
            order.paid=True
            order.save()
            Cart=cart.objects.get(user=request.user)
            order_item=order.order_item_set.all()
            send_mail(
                "Order Placed...",  #Subject of mail
                "Order has been placed successfully and will be delivered soon...",  #upper line is mail
                settings.EMAIL_HOST_USER, #who sends email (ADMIN)
                ["jari.jafri21@gmail.com","jjafri75@gmail.com","priyanka.vibhute@itvedant.com"], #to whom we want to send email to ...can be multiple users
                fail_silently=False, #throws exception
                html_message=render_to_string("email.html",{"items":order_item})
                )
            Cart.delete()
            return render(request,"success.html",{})
        