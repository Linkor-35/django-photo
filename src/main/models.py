from django.db import models
import uuid


class Order(models.Model):
    CHOISE = [
        ('10x15','10x15'),
        ('15x21','15x21'),
        ('21x30','21x30'),
        ('30x40','30x40'),
        ('30x45','30x45'),
    ]

    PHOTO_TYPE = [
        ('Матовая', 'Матовая'),
        ('Глянцевая','Глянцевая'),
    ]

    # order_uidd = models.CharField('Идентификатор заказа', default=" ", max_length=5)
    photo_size = models.CharField('Размер фото',choices=CHOISE, default=CHOISE[0], max_length=10)
    photo_type = models.CharField('Тип фото',choices=PHOTO_TYPE, default=PHOTO_TYPE[0], max_length=10)
    img = models.ImageField('Загрузка фото', upload_to='photos/')
    phone = models.CharField('Телефон для связи', max_length=12, default="")
    count = models.IntegerField("Колличество фото:", default=1)

    # def save(self, commit=True):


    # def tuple(self):
    #     return self.order_uidd

    class Meta():
        verbose_name = "Заказы"
        verbose_name_plural = "Заказ"

    objects = models.Manager()
    

