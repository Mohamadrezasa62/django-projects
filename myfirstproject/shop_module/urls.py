from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product-detail'),
    # path('<int:id>/', views.ProductDetail.as_view(), name='product-detail'),
    path('test', views.TestView.as_view(), name='test-view'),
    path('add-favorite/<int:id>', views.add_favorite, name='add-favorite')
]
