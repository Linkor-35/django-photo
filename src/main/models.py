from django.db import models


class Order(models.Model):
    order_uidd = "uuid"
    photo_size = models.CharField('Размер фото', max_length=10)
    photo_type = models.BooleanField("Матовая?")
    img = models.ImageField('Загрузка фото', upload_to='photos/')
    phone = models.CharField('Телефон для связи', max_length=12, default="")

    def tuple(self):
        return self.order_uidd, self.phone

    class Meta():
        verbose_name = "Заказы"
        verbose_name_plural = "Заказ"

    objects = models.Manager()
    

