from django import forms  #for django forms 
from first_app.models import Order
from first_app.models import order_item


class order_form(forms.ModelForm):
    class Meta:  #meta tells everything about data
        model=Order
        fields="__all__"
        exclude=["order_id","user","paid"]