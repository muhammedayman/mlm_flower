# Generated by Django 3.0.5 on 2020-07-12 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20200712_1213'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carts',
            new_name='Cart',
        ),
    ]
