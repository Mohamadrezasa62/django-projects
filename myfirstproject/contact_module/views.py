from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, FormView

from contact_module.forms import ContactUsForm
from contact_module.models import ContactUs
from site_module.models import SiteSetting


# Create your views here.


# def contact_us_view(request: HttpRequest):
#     return render(request, 'contact_module/contact_us.html')


# class CreateContactUs(CreateView):
#     # model = ContactUs
#     # fields = ['subject', 'email', 'name', 'text']
#     form_class = ContactUsForm
#     template_name = 'contact_module/contact_us.html'
#     success_url = '/contact-us'

# class CreateContactUs(View):
#     def get(self, request: HttpRequest):
#         form = ContactUsForm()
#         return render(request, 'contact_module/contact_us.html', context={'form': form})
#
#     def post(self, request: HttpRequest):
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             # if we have ModelForm
#             form.save()
#             # if the form will not be ModelForm
#             # cleaned_data = form.cleaned_data
#             # contact_instantiate = ContactUs(
#             #     subject=cleaned_data.get('subject'),
#             #     email=cleaned_data.get('email'),
#             #     name=cleaned_data.get('name'),
#             #     text=cleaned_data.get('text'),
#             # )
#             # contact_instantiate.save()
#         else:
#             return render(request, 'contact_module/contact_us.html', context={'form': form})
#
#         # form = ContactUsForm()
#         return redirect(reverse('contact-us'))

class CreateContactUs(FormView):
    form_class = ContactUsForm
    template_name = 'contact_module/contact_us.html'
    success_url = '/contact-us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['setting'] = site_setting
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def create_contact_us(request: HttpRequest):
    if request.method == 'POST':
        print('salam', request.POST, request.FILES)
        return render(request, 'contact_module/contact_us.html')
    elif request.method == 'GET':
        return render(request, 'contact_module/contact_us.html')


def social_media_components_partial(request: HttpRequest):
    context = {}
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context['setting'] = site_setting
    return render(request, 'contact_module/social_media_components/index.html', context=context)
