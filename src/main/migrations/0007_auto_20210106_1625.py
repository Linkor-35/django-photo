# Generated by Django 3.1.4 on 2021-01-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210106_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_uidd',
            field=models.CharField(default=' ', max_length=5, verbose_name='Идентификатор заказа'),
        ),
    ]
