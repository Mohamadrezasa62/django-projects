from django.contrib import admin

from site_module.models import SiteSetting, SocialMedias, FooterBoxHeader, FooterBoxItems, Slider

# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(SocialMedias)
admin.site.register(FooterBoxHeader)
admin.site.register(FooterBoxItems)
admin.site.register(Slider)
