from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from article_module.models import Article, ArticleCategory


# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_module/article_list/index.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs.get('category')
        if category:
            # Article.objects.filter(selected_categories__url_title=)
            queryset = queryset.filter(selected_categories__url_title__iexact=category)
        return queryset


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail/index.html'
    model = Article
    context_object_name = 'article'


def article_category_component_partial(request: HttpRequest):
    context = {
        'category': ArticleCategory.objects.filter(is_active=True, parent=None)
    }
    return render(request, 'article_module/category_component/index.html', context)
