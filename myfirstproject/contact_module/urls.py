from django.urls import path
from . import views
urlpatterns = [
    path('', views.CreateContactUs.as_view(), name='contact-us'),
    # path('test', views.create_contact_us, name='test')
]
