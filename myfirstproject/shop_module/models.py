from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import time


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


MemberShip = [
    ('B', 'Beginner'),
    ('G', 'Gold'),
    ('S', 'Silver'),
]


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=500, db_index=True, verbose_name='عنوان در url')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return f"({self.title} - {self.url_title})"

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های محصولات'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='برند', db_index=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه', null=True)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, verbose_name='امتیاز')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    slug = models.SlugField(blank=True, default='', db_index=True, unique=True, verbose_name='اسلاگ')
    tag = models.ManyToManyField(Tag, verbose_name='تگ', related_name='products')
    membership = models.CharField(max_length=1, choices=MemberShip, default='Beginner')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='دسته بندی', null=True,
                                 related_name='products')
    information = models.OneToOneField('ProductInformation', on_delete=models.CASCADE, verbose_name='اطلاعات مربوطه',
                                       null=True, related_name='products')
    is_new = models.BooleanField(default=True, verbose_name='جدید/قدیمی')
    date_joined = models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ایجاد')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True)
    last_watched_time = models.DateTimeField(null=True, verbose_name='تاریخ آخرین بازدید توسط کاربران')
    count_number_of_views = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='تعداد مشاهده ها')
    image = models.FileField(upload_to='admin-uploads', null=True, blank=True, verbose_name='تصویر محصول')
    # 2024-03-11 19:58:29.735387

    def __str__(self):
        return f"{self.title} price: {self.price}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, db_index=True, verbose_name='رنگ بندی محصول')
    size = models.CharField(max_length=250, db_index=True, verbose_name='سایز محصول')

    def __str__(self):
        return f"{self.size}-{self.color}"

    class Meta:
        verbose_name = 'اطلاعات محصول'
        verbose_name_plural = 'کلیه اطلاعات محصولات'


class UserUploadFile(models.Model):
    file = models.ImageField(upload_to='admin-uploads', blank=True, null=True)
