from django.db.models import QuerySet, Count, Max
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from shop_module.models import ProductBrand, Product
from article_module.models import Article, ArticleCategory, ArticleComments, ArticleCommentsAnswer
from site_module.models import SiteSetting



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
        queryset: QuerySet = super().get_queryset()
        queryset = queryset.filter(is_active=True).prefetch_related('author')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = ArticleComments.objects.filter(article_id=self.object.id).prefetch_related(
            'responses',
            'auther')
        return context


def article_category_component_partial(request: HttpRequest):
    # print(Product.objects.aggregate(maximom=Max('rate')))
    context = {
        'banners': SiteSetting.objects.filter(is_main_setting=True).first().banners.all(),
        'category': ArticleCategory.objects.filter(is_active=True, parent=None),
        'brands': ProductBrand.objects.all().annotate(products_count=Count('product'))
    }
    return render(request, 'article_module/category_component/index.html', context)


def add_article_comment(request: HttpRequest):
    if request.method == "POST":
        article_id = request.POST.get("article_id")
        form = CommentForm(request.POST)
        comment_id = request.POST.get('comment_id')
        is_answer = request.POST.get('is_answer')
        if form.is_valid():
            if is_answer == "0":
                comment = ArticleComments(article_id=article_id, text=form.cleaned_data.get('text'),
                                          auther=request.user)
                comment.save()
                return redirect(reverse('article-detail', args=[article_id]))
            else:
                comment = ArticleCommentsAnswer(text=form.cleaned_data.get('text'),
                                                auther=request.user, comment_id=comment_id)
                comment.save()
                return redirect(reverse('article-detail', args=[article_id]))
        return render(request, 'article_module/article_detail/index.html',
                      {'form': form,
                       'article': Article.objects.filter(
                           pk=article_id, is_active=True).first()})
