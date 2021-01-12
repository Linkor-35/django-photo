from django.contrib import admin
from .models import Order, Photo

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'is_done',
        'order_uidd',
        'phone',
    ]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
        list_display = [
        'order',
        'count',
        'photo_uuid',
        'photo_size',
        'img',
    ]

