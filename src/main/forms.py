from django import forms
from .models import Order, Photo


class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = (
            "phone",
            'order_uidd',
            )

class PhotoForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ('photo_size', 'photo_type', 'img', 'count')
