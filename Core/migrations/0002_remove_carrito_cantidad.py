# Generated by Django 4.0.4 on 2022-06-20 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='Cantidad',
        ),
    ]