from django.urls import path

from article_module import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
]
