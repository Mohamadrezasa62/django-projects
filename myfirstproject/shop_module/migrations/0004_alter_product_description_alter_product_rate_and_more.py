# Generated by Django 4.2.3 on 2024-03-10 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module', '0003_product_short_description_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=300, null=True, verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True, verbose_name='اسلاگ'),
        ),
    ]