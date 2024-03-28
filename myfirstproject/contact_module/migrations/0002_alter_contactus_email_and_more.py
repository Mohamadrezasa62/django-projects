# Generated by Django 4.2.3 on 2024-03-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=300, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='دیده شده/نشده'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=300, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='response',
            field=models.TextField(verbose_name='پاسخ'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=300, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
    ]