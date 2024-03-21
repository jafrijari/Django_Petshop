from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from core.models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        phone=request.POST.get('phone_field')
        #print(username,email) ... to check if register successfull or not
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("Username already exists")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    print("Email already exists")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data = Customer(user=user,phone_field=phone)
                    data.save()

                    #code for login of user will come here
                    #after registration no need to re-login again
                    our_user=authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
        else:
            print("Error")
            return redirect('user_register')

        
    return render(request,'accounts/register.html')

def user_login(request):
    if request.method == "POST":
        username= request.POST.get('username')
        email=request.POST.get('email')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request,'accounts/login.html')
    




def user_logout(request):
    logout(request)
    return redirect('/')


