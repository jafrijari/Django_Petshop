from django.urls import path,include
from accounts import views
# or, from accounts.views importfrom accounts.views import  user_login,user_logout,user_register 

urlpatterns=[
    path('user_register',views.user_register,name="user_register"),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
]