# Generated by Django 2.1.5 on 2021-01-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0002_products_products_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
