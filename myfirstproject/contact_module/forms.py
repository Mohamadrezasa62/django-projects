from attr import attr
from django import forms
from django.core.validators import MinLengthValidator

from contact_module.models import ContactUs


# class ContactUsForm(forms.Form):
#     subject = forms.CharField(label='موضووععع', max_length=25,
#                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}),
#                               error_messages={
#                                   'required': 'باید سابجکت بزنی',
#                                   'max_length': 'خییلی زیاد وارد کردی!'
#                               }, validators=[MinLengthValidator(5)])
#     name = forms.CharField(label='نام', max_length=200,
#                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
#                            error_messages={
#                                'required': 'باید نامت رو بزنی',
#                                'max_length': 'خییلی زیاد وارد کردی!'
#                            }, validators=[])
#     email = forms.EmailField(label='ایمیل', max_length=110,
#                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
#                              error_messages={
#                                  'required': 'باید ایمیل بزنی',
#                                  'max_length': 'خییلی زیاد وارد کردی!'
#                              }, validators=[])
#     text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 10,
#                                                         'placeholder': 'متن پیام'}),
#                            error_messages={
#                                'required': 'باید متن پیام رو وارد کنی!'
#                            })
    # is_read_by_admin = forms.BooleanField()
    # response = forms.Textarea()

class ContactUsForm(forms.ModelForm):
    # subject = forms.CharField(required=False)
    class Meta:
        model = ContactUs
        fields = ['email', 'subject', 'name', 'text']
        widgets = {
            "subject": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'موضوع',
                       }),
            "name": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'نام',
                       }),
            "text": forms.Textarea(
                attrs={'id': 'message', 'class': 'form-control', 'placeholder': 'متن پیام',
                       'rows': 8}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید',
                                             # 'oninvalid': 'this.setCustomValidity("ایمیل نمیتواند خالی باشد")',
                                             # 'oninput': 'setCustomValidity("ایمیل خود را درست وارد کنید")'
                                             })
        }
        labels = {
            'subject': 'موضوع تیکت',
            'email': 'ایمیل',
            'name': 'نام کاربر',
            'text': 'متن شما',
        }
        error_messages = {
            'subject': {
                'required': 'واجبه!'
            },
            'email': {
                'required': 'وارد کردن ایمیل ضروری است!',
                'invalid': 'ایمیل وارد شده صحیح نبود!'
            }

        }

