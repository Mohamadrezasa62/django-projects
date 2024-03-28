from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name="آدرس ایمیل", blank=True, unique=True, db_index=True)
    phone = models.CharField(max_length=20, null=True, verbose_name='تلفن همراه')
    location = models.TextField(null=True, blank=True, verbose_name="آدرس")
    email_confirm_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='کد فعالسازی ایمیل', db_index=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return str(self.id)
