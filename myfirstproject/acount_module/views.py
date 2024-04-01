from django.conf import settings
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import DetailView

from helper_module.send_mail import send_mail_from_site
from .forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from .models import User


# Create your views here.


class RegisterView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm()
        return render(request, 'acount_module/register/index.html', {'form': register_form})

    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user = User(email=email, username=email, is_active=False)
            user.email_confirm_code = get_random_string(length=72)
            user.set_password(password)

            context = {
                'email_active_code': user.email_confirm_code
            }
            send_mail_from_site('فعالسازی حساب کاربری',
                                'acount_module/send_active_email/index.html',
                                context,
                                [email])

            user.save()
            return redirect(reverse('login-page'))

        return render(request, 'acount_module/register/index.html', {'form': form})


class LoginView(View):
    def get(self, request: HttpRequest):
        form = LoginForm()
        return render(request, 'acount_module/login/index.html', {'form': form})

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            try:
                user = User.objects.get(email=cleaned_data.get('email'))
                if user.check_password(cleaned_data.get('password')):
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse('main-page'))
                    else:
                        form.add_error('email',
                                       'ایمیل شما تایید نشده است، برای فعالسازی به ایمیل خود مراجعه کنید و بر روی لینک فعالسازی ارسالی کلیک کنید!')
                else:
                    form.add_error('password', 'ایمیل یا رمز عبور وارد شده اشتباه میباشد!')
                    form.add_error('email', 'ایمیل یا رمز عبور وارد شده اشتباه میباشد!')

            except:
                form.add_error('email', 'ایمیل یا رمز عبور وارد شده اشتباه میباشد!')
                form.add_error('password', 'ایمیل یا رمز عبور وارد شده اشتباه میباشد!')

        return render(request, 'acount_module/login/index.html', {'form': form})


def logout_view(request: HttpRequest):
    if request.method == 'GET':
        logout(request)
        return redirect(reverse('login-page'))


def activate_via_email(request: HttpRequest, email_active_code):
    print('salam')
    if request.method == 'GET':
        user = get_object_or_404(User, email_confirm_code=email_active_code)
        if not user.is_active:
            user.is_active = True
            user.email_confirm_code = get_random_string(length=72)
            user.save()
            return redirect(reverse('login-page'))
        else:
            raise Http404()


class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forgot_form = ForgotPasswordForm()
        return render(request, 'acount_module/forgot_password/index.html', {
            'form': forgot_form
        })

    def post(self, request: HttpRequest):
        forgot_form = ForgotPasswordForm(request.POST)
        if forgot_form.is_valid():
            user = User.objects.filter(email__iexact=forgot_form.cleaned_data.get('email'))
            if user.exists():
                user = user.first()
                context = {
                    'active_code': user.email_confirm_code
                }
                send_mail_from_site(
                    'فراموشی رمز عبور ورود به سایت',
                    'acount_module/send_forgot_password/index.html',
                    context,
                    [user.email],
                )
                return redirect(reverse('login-page'))
            else:
                forgot_form.add_error('email', 'ایمیل وارد شده صحیح نمیباشد!')

        return render(request, 'acount_module/forgot_password/index.html', {
            'form': forgot_form
        })


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user = User.objects.filter(email_confirm_code__iexact=active_code)
        if user.exists():
            user = user.first()
            if user.is_active:
                reset_form = ResetPasswordForm()
                return render(request, 'acount_module/reset_password/index.html', {
                    'form': reset_form,
                    'active_code': active_code
                })
        raise Http404()

    def post(self, request: HttpRequest, active_code):
        reset_form = ResetPasswordForm(request.POST)
        if reset_form.is_valid():
            user = User.objects.filter(email_confirm_code__iexact=active_code)
            if user.exists():
                user = user.first()
                user.set_password(reset_form.cleaned_data.get('password'))
                user.email_confirm_code = get_random_string(length=72)
                user.is_active = True
                user.save()
                return redirect(reverse('login-page'))
            else:
                reset_form.add_error('password', 'شما ثبت نام نکرده اید که مجاز به تغییر رمز عبور باشید!')
        return render(request, 'acount_module/reset_password/index.html', {
            'form': reset_form,
        })


class UserProfileView(DetailView):
    model = User
    template_name = 'acount_module/user_profile/index.html'
    context_object_name = 'user'

