from django.urls import path

from home_module import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main-page"),
    path("partial-slider", views.slider_partial, name='partial_slider'),
    path("header-partial", views.header_partial, name='header-partial'),
    path("footer-partial", views.footer_partial, name='footer-partial'),
    path("about-us/", views.AboutUsView.as_view(), name='about-us'),
]