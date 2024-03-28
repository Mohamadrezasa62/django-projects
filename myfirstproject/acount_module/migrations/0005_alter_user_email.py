# Generated by Django 4.2.3 on 2024-03-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount_module', '0004_alter_user_email_confirm_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]