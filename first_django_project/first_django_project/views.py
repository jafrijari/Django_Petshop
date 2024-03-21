from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from forms import register_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact_me.html")

def home(request):
    username=request.session.get("current_user",None)
    return render(request,"index.html",{"username":username})


@login_required(login_url="/login/")
def search(request):
    query=request.GET.get('query','')
    print(query)
    products=product.objects.all().filter(product_name__icontains=query)
    return render(request,'search.html',{"all_products":products})

def register(request):
    if request.method=="POST":
        #form=UserCreationForm(request.POST)
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=register_form()
    return render(request,"register.html",{"form":form})




def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
           #Authrntication
            
            user = authenticate(username = username,password = password)      #calling #Authentiucate

            if user is not None:
                login(request,user)  #passing current http request and user object
                request.session["current_user"]=user.get_username()
                return HttpResponseRedirect("/")

    else:
     form = AuthenticationForm()
     return render(request,"login.html",{"form":form})
    
#user Logout Function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")




    