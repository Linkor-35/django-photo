# Generated by Django 3.1.4 on 2021-01-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_order_order_uidd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Колличество фото:'),
        ),
    ]
