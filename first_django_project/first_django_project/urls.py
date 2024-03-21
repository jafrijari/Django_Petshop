"""
URL configuration for first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from first_app import views
from product import views as p
from django.conf.urls.static import static
from first_django_project import settings

from .views import about
from .views import contact
from .views import home
from .views import search
from .views import register,user_login,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.demo_home),
    #path('',views.firstpage,name="homepage"),  #no path as we want it @ home page
    path('about_us',views.about_us),
    path('contact_us',views.contact_us),
    path('users',views.users),
    path('admins',views.admins),
    #path('register',views.register),
    path('submit',views.submit),
    path("class",views.first_class_based_view.as_view()),
    path("details",views.second_class_based_view.as_view(name="nitya")),
    path("product/",include('product.urls')),
    path("about/",about),
    path("contact_me/",contact),
    path("",home),
    path("search/",search),
    path("register/",register),
    path("login/",user_login),
    path("logout/",user_logout,name="logout"),
    path("",include("cart.urls"))


]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
