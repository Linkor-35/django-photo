# Generated by Django 3.1.4 on 2021-01-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210104_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_uidd',
            field=models.CharField(default='626122612', max_length=10, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_uuid',
            field=models.CharField(default='1723554253', max_length=10, verbose_name='Идентификатор'),
        ),
    ]