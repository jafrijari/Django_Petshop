from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class register_form(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        #labels={"username":"unique username","last_name":"l_name"} #this is to change pre defined labels to custom 
        #fields="__all__" #__all__ gives all variables(fields)


