from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from article_module.models import Article, ArticleCategory, ArticleComments


# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_module/article_list/index.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        category = self.kwargs.get('category')
        if category:
            # Article.objects.filter(selected_categories__url_title=)
            queryset = queryset.filter(selected_categories__url_title__iexact=category)
        return queryset


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail/index.html'
    model = Article
    context_object_name = 'article'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


def article_category_component_partial(request: HttpRequest):
    context = {
        'category': ArticleCategory.objects.filter(is_active=True, parent=None)
    }
    return render(request, 'article_module/category_component/index.html', context)


def add_article_comment(request: HttpRequest):
    if request.method == "POST":
        form = CommentForm(request.POST)
        article_id = request.POST.get("article_id")
        if form.is_valid():
            comment = ArticleComments(article_id=article_id, text=form.cleaned_data.get('text'),
                                      auther=request.user)
            print(comment.clean_fields())
            comment.save()
            return redirect(reverse('article-detail', args=[article_id]))
        return render(request, 'article_module/article_detail/index.html', {'form': form,
                                                                            'article': Article.objects.filter(
                                                                                pk=article_id, is_active=True).first()})
