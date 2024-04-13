from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from site_module.models import SiteSetting, FooterBoxHeader, Slider


# Create your views here.


# the main function based View

def slider_partial(request: HttpRequest):
    context = {
        'sliders': Slider.objects.filter(is_active=True)

    }
    return render(request, 'slider/index.html', context)


def header_partial(request: HttpRequest):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, 'header/index.html', {
        'setting': site_setting
    })


def footer_partial(request: HttpRequest):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_box_headers = FooterBoxHeader.objects.all().prefetch_related('items')
    return render(request, 'footer/index.html', {
        'setting': site_setting,
        'footer_headers': footer_box_headers,
    })


def main_page(request: HttpRequest):
    print('salam', request.resolver_match.url_name)
    if request.method == 'GET':
        context = {}
        return render(request, "home_module/main_page/index.html", context)


class MainPage(View):

    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, "home_module/main_page/index.html", context)


# class MainPage(TemplateView):
#     template_name = 'home_module/main_page/index.html'
#     # method 1 to add extera context
#     extra_context = {
#         'name': 'lkk'
#     }
#     # method 2 to add extera context
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data()
#     #     context['name'] = 'salam'
#     #     return context

class AboutUsView(View):
    def get(self, request: HttpRequest):
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context = {
            'setting': site_setting,
        }
        return render(request, 'home_module/about_us/index.html', context)
