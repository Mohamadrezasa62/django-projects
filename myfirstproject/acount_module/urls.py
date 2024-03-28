from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('logout/', views.logout_view, name='logout'),
    path('activate-email/<slug:email_active_code>/', views.activate_via_email, name='activate-email'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<slug:active_code>', views.ResetPasswordView.as_view(), name='reset-password'),
]
