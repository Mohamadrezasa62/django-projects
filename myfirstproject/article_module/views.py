from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from article_module.models import Article


# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_module/article_list/index.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 1


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail/index.html'
    model = Article
    context_object_name = 'article'

