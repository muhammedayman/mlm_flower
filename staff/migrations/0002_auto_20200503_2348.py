# Generated by Django 3.0.5 on 2020-05-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
