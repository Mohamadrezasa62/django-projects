from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from acount_module.models import User


# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    parent = models.ForeignKey('ArticleCategory', blank=True, null=True, on_delete=models.CASCADE, verbose_name='والد',
                               related_name='children')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'


class Article(models.Model):
    selected_categories = models.ManyToManyField(ArticleCategory, blank=True, verbose_name='دسته بندی های مربوطه')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name='نویسنده')
    rate = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='امتیاز')
    image = models.ImageField(upload_to='admin-uploads/article_images', null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
