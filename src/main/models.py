from django.db import models
import uuid


def get_uuid():
    uid = str(uuid.uuid4().fields[0])
    return uid


class Order(models.Model):
    order_uidd = models.CharField('Идентификатор', default=get_uuid(), max_length=10)
    is_done = models.BooleanField('Выполнен?', default=False)
    phone = models.CharField('Телефон для связи', max_length=20)

    class Meta():
        verbose_name = "Заказы"
        verbose_name_plural = "Заказ"


class Photo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    photo_uuid = models.CharField('Идентификатор', default=get_uuid(), max_length=10)

    STATUS_CHOICES = [
        ('10x15','10x15'),
        ('15x21','15x21'),
        ('21x30', '21x30'),
        ('30x40','30x40'),
        ('30x45','30x45'),
    ]

    photo_size = models.CharField('Размер фото', max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    photo_type = models.BooleanField("Матовая?")
    img = models.ImageField('Загрузка фото', upload_to='photos/')
    count = models.IntegerField('Кол-во', default=1)


    class Meta():
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотография"

    

