# Generated by Django 4.2.3 on 2024-03-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module', '0015_alter_useruploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploadfile',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='admin-uploads'),
        ),
    ]