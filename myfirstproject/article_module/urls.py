from django.urls import path

from article_module import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('cat/<slug:category>', views.ArticleListView.as_view(), name='article-list-by-cat'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add-article-comment', views.add_article_comment, name='add-article-comment'),
]
