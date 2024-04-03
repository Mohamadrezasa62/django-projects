from django.db import models


# Create your models here.
class SocialMedias(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام برنامه')
    url = models.CharField(max_length=255, verbose_name='لینک برنامه')
    logo = models.ImageField(upload_to='admin-uploads/logos', verbose_name='لوگو برنامه')

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.name


class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی/غیر اصلی')
    site_name = models.CharField(max_length=200, verbose_name='نام نمایشی سایت')
    site_url = models.CharField(max_length=255, verbose_name='آدرس سایت')
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='فکس')
    email = models.CharField(max_length=200, blank=True, null=True, verbose_name='آدرس ایمیل')
    copyright_text = models.TextField(max_length=200, verbose_name='متن کپی رایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    about_us_text = models.TextField(verbose_name='متن درباره ما')
    site_logo = models.ImageField(upload_to='admin-uploads/user-uploads', verbose_name='تصویر سایت')
    social_medias = models.ManyToManyField(SocialMedias, blank=True, verbose_name='شبکه های اجتماعی')
    banners = models.ManyToManyField('SiteBanner', null=True, blank=True, verbose_name='بنرها')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'کلیه تنظیمات'

    def __str__(self):
        return f'تنظیمات شماره {self.id}'


class SiteBanner(models.Model):
    image = models.ImageField(upload_to='upload-files/admin-uploads/banners', verbose_name='تصویر')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'


class FooterBoxHeader(models.Model):
    title = models.CharField(max_length=255, verbose_name='نام')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرتیتر'
        verbose_name_plural = 'سرتیتر ها'


class FooterBoxItems(models.Model):
    title = models.CharField(max_length=255, verbose_name='نام آیتم')
    url = models.CharField(max_length=300, verbose_name='لینک')
    footer_box_header = models.ForeignKey(FooterBoxHeader, on_delete=models.CASCADE, verbose_name='سرتیتر مربوطه',
                                          related_name='items')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'آیتم'
        verbose_name_plural = 'آیتم ها'


class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان url')
    url = models.URLField(max_length=300, verbose_name='url')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='admin-uploads/slider_images', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'
