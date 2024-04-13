from django.db.models import QuerySet, Count, Max
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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
    if request.user.is_authenticated:
        user = request.user
        text = request.GET.get('text')
        article_id = int( request.GET.get('article_id'))
        is_answer = int(request.GET.get('is_answer'))
        comment_id = int(request.GET.get('comment_id'))
        print(text, article_id, is_answer, comment_id)
        if is_answer == 0:
            comment = ArticleComments(article_id=article_id, auther=user, text=text)
            comment.save()
            return redirect('article-list')
            # or
            # render('*.html')
            # or
            # return HttpResponse('salam')
        else:

            comment = ArticleCommentsAnswer(auther=user, text=text, comment_id=comment_id)
            comment.save()
            return render(request, 'article_module/article_detail/comments_component/index.html',
                          context={'comments': ArticleComments.objects.all()})
    return HttpResponse('salam')

    # if request.method == "GET":
    #     print('im in view')
    #     dicto = {
    #         'text': 'bjbj',
    #         'name': 'vhvhv'
    #     }
    #     form = CommentForm(dicto)
    #     article_id = request.GET.get("article_id")
    #     comment_id = request.GET.get('comment_id')
    #     is_answer = request.GET.get('is_answer')
    #     print('s:', form.text, form.name)
    #     if form.is_valid():
    #         print('form valid')
    #         if is_answer == "0":
    #             comment = ArticleComments(article_id=article_id, text=form.cleaned_data.get('text'),
    #                                       auther=request.user)
    #             comment.save()
    #             return redirect(reverse('article-detail', args=[article_id]))
    #         else:
    #             comment = ArticleCommentsAnswer(text=form.cleaned_data.get('text'),
    #                                             auther=request.user, comment_id=comment_id)
    #             comment.save()
    #             return redirect(reverse('article-detail', args=[article_id]))
    #     return render(request, 'article_module/article_detail/index.html',
    #                   {'form': form,
    #                    'article': Article.objects.filter(
    #                        pk=article_id, is_active=True).first()})
