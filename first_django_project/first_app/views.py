from django.shortcuts import render,HttpResponse
from django.views import View #for class based views

# Create your views here.

def demo_home(request):
    #code here
    return HttpResponse("first view")

def firstpage(request):
    #code here
    return HttpResponse("<h1>first page</h1>")

def about_us(request):
    return HttpResponse("<h1> About US</h1>")

def contact_us(response):
    return HttpResponse("email us - abc@xyz.com")

def users(request):

    student={"id":101,"name":"jari","age":23} #dictionary

    return render(request,"index.html",student) #without dictionary first
    
def admins(request):
    school={"school_name":"SJHS", "school_code":1,"school_add":"colaba"}
    return render(request,"index2.html",school)


def register(request):
    return render(request,"register.html")

def submit(request):
    if request.method=="POST":
        return render(request,"submit.html")
    if request.method=="GET":
        return render(request,"register.html")
#this func checks the request
#if type get then it sends us to register
#if type post then lets us go to submit page
    

#class based view:
class first_class_based_view(View):
    def get(self,request):
        return HttpResponse("Class Based View -GET")

class second_class_based_view(View):
    name="nisha"
    def get(self,request):
        return render(request,"detail.html",{"name":self.name})