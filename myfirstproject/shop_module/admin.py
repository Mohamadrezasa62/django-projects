from attr.filters import include
from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete', 'category', 'date_joined']
    list_filter = ['is_active', 'title', 'category']
    list_editable = ['is_active', 'is_delete']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Tag)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductInformation)
admin.site.register(models.ProductBrand)
