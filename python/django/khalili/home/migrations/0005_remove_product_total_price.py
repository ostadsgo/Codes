# Generated by Django 4.2.6 on 2024-01-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_product_discounting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]
