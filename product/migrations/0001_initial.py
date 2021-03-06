# Generated by Django 3.0.5 on 2020-07-12 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0003_auto_20200712_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('context_text', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('ratings', models.PositiveIntegerField()),
                ('price', models.FloatField(default=0)),
                ('net_amout', models.FloatField(default=0)),
                ('gross_amount', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('offer', models.FloatField(default=0)),
                ('date_order', models.DateTimeField(blank=True, null=True)),
                ('date_dispatch', models.DateTimeField(blank=True, null=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('user_delivery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_delivery', to='staff.Staff')),
                ('user_distributer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_distributer', to='staff.Staff')),
                ('user_staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_staff', to='staff.Staff')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_price', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField()),
                ('offer', models.FloatField(default=0)),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_sale', to='product.Products')),
            ],
            options={
                'db_table': 'product_sales',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.Category')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Products')),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
    ]
