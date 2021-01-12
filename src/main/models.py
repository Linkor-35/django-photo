from django.db import models
import uuid
<<<<<<< HEAD


class Order(models.Model):
    CHOISE = [
        ('10x15','10x15'),
        ('15x21','15x21'),
        ('21x30','21x30'),
=======


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
>>>>>>> c34899ca9fad5e2c6cb9a49761b26fa5e3b65a7b
        ('30x40','30x40'),
        ('30x45','30x45'),
    ]

<<<<<<< HEAD
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
=======
    photo_size = models.CharField('Размер фото', max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    photo_type = models.BooleanField("Матовая?")
    img = models.ImageField('Загрузка фото', upload_to='photos/')
    count = models.IntegerField('Кол-во', default=1)

>>>>>>> c34899ca9fad5e2c6cb9a49761b26fa5e3b65a7b

    class Meta():
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотография"

    

