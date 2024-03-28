from django.db import models

# Create your models here.


class ContactUs(models.Model):
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    name = models.CharField(max_length=300, verbose_name='نام')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='دیده شده/نشده')
    response = models.TextField(verbose_name='پاسخ', null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'
