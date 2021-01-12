from django import forms
from .models import Order, Photo




class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
<<<<<<< HEAD
        fields = ('photo_size', 'photo_type', 'img', 'phone', 'count')
=======
        fields = (
            "phone",
            'order_uidd',
            )

class PhotoForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ('photo_size', 'photo_type', 'img', 'count')
>>>>>>> c34899ca9fad5e2c6cb9a49761b26fa5e3b65a7b
