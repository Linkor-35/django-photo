from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ('photo_size', 'photo_type', 'img', 'phone')