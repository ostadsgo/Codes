# Generated by Django 4.2.6 on 2024-02-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
