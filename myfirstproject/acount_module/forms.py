from django import forms
from django.core.exceptions import ValidationError

from acount_module.models import User


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', }),
                                       label='تکرار رمز عبور')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('رمز عبور و تکرار رمز عبور مطابقت ندارند!')

    class Meta:
        model = User
        fields = ['email', 'password']
        error_messages = {
            'password': {
                'required': 'وارد کردن رمز عبور اجباری است!',
                'max_length': 'رمز عبور وارد شده دارای طول غیر مجاز است!',
            },
            'email': {
                'required': 'وارد کردن ایمیل اجباری است!',
                'max_length': 'ایمیل وارد شده دارای طول غیر مجاز است!',
            }
        }
        labels = {
            'password': 'رمز عبور'
        }


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
        'required': 'وارد کردن ایمیل اجباری است!',
        'max_length': 'ایمیل وارد شده دارای طول غیر مجاز است!',
    }, label='آدرس ایمیل')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={
                                   'required': 'وارد کردن رمز عبور اجباری است!',
                                   'max_length': 'رمز عبور وارد شده دارای طول غیر مجاز است!',
                               }, label='رمز عبور')


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=120, widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label='آدرس ایمیل', error_messages={
            'required': 'ایمیل نمیتواند خالی باشد!',
            'max_length': 'طول ایمیل وارد شده بیش از حد مجاز میباشد!',
        })


class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='رمز عبور جدید',
                               error_messages={
                                   'required': 'وارد کردن این فیلد اجباری است!',
                               })
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                       label='تکرار رمز عبور جدید',
                                       error_messages={
                                           'required': 'وارد کردن این فیلد اجباری است!',
                                       })

    def clean_confirm_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('password') == cleaned_data.get('confirm_password'):
            return cleaned_data.get('confirm_password')
        raise ValidationError('تکرار رمز عبور با رمز عبور باید یکسان باشند!')
