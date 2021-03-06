# Generated by Django 3.1.4 on 2021-01-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_order_order_uidd'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_uidd',
            field=models.CharField(default='33544', max_length=5, verbose_name='Идентификатор заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='photo_size',
            field=models.CharField(choices=[('10x15', '10x15'), ('15x21', '15x21'), ('21x30', '21x30'), ('30x40', '30x40'), ('30x45', '30x45')], default=('10x15', '10x15'), max_length=10, verbose_name='Размер фото'),
        ),
        migrations.AlterField(
            model_name='order',
            name='photo_type',
            field=models.CharField(choices=[('Матовая', 'Матовая'), ('Глянцевая', 'Глянцевая')], default=('Матовая', 'Матовая'), max_length=10, verbose_name='Тип фото'),
        ),
    ]
