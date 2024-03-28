from django.contrib import admin
from .models import ArticleCategory, Article
# Register your models here.
# class


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        return super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
