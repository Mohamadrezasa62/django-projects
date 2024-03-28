from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('accounts/profile/', views.AccountProfile.as_view(), name='account_profile'),
]
