# Generated by Django 4.2.3 on 2024-03-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module', '0009_product_count_number_of_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_watched_time',
            field=models.DateTimeField(null=True, verbose_name='تاریخ آخرین بازدید توسط کاربران'),
        ),
    ]
