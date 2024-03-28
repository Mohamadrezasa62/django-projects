import time

from django.urls import reverse
from django.utils import timezone

from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from .forms import TestForm
from .models import Product, ProductCategory, UserUploadFile
from django.db.models import Avg, Max, Min, Sum, Count


# Create your views here.


# def product_list(request: HttpRequest):
#     products = Product.objects.filter(is_active=True)
#     number_of_products = products.count()
#     average_of_rate = products.aggregate(average_rete=Avg('rate'))['average_rete']
#
#     return render(request, 'shop_module/product-list.html', {
#         'products': products,
#         # 'number_of_products': number_of_products,
#         # 'average_of_rate': average_of_rate
#     })


class ProductList(ListView):
    template_name = 'shop_module/product-list.html'
    context_object_name = 'products'
    model = Product
    ordering = ['-count_number_of_views']
    # paginate_by = 1

    # queryset = Product.objects.filter(is_active=True, is_delete=False)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True, is_delete=False)


# class ProductList(TemplateView):
#     template_name = 'shop_module/product-list.html'
#     extra_context = {
#         'products': Product.objects.filter(is_active=True, is_delete=False).order_by('-id')
#     }


# def product_detail(request: HttpRequest, slug):
#     # try:
#     #     product = Product.objects.get(pk=ProductID)
#     # except:
#     #     raise Http404()
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'shop_module/product-detail.html', {
#         'product': product,
#     })


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop_module/product-detail.html'

    def get_context_data(self, **kwargs):
        obj = self.object
        request = self.request
        context = super().get_context_data()
        context['related_product'] = Product.objects.filter(category=obj.category)
        product_id_favorite = request.session.get('favorite_product')
        context['is_favorite'] = obj.id == product_id_favorite
        return context

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.last_watched_time = time.strftime('%Y-%m-%d %H:%M:%S')
        obj.count_number_of_views += 1
        obj.save()
        return obj


# class ProductDetail(TemplateView):
#     template_name = 'shop_module/product-detail.html'
#
#     def get_context_data(self, **kwargs):
#         product = get_object_or_404(Product, slug=kwargs.get('slug'))
#         context = super(ProductDetail, self).get_context_data()
#         context['product'] = product
#         return context

# def saveer(file):
#     with open('upload-files/admin-uploads/t.jpj', 'wb+') as my_file:
#         for chunk in file.chuncks():
#             my_file.write(chunk)


class TestView(View):

    def get(self, request: HttpRequest):
        form = TestForm()
        return render(request, 'test_view/test_view.html', {
            'form': form
        })

    def post(self, request: HttpRequest):
        print(request.POST, request.FILES)
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            # saveer(form.cleaned_data.get('file'))
            form.save()
            # UserUploadFile.objects.create(file=form.cleaned_data.get('file'))
            return redirect(reverse('test-view'))
        return render(request, 'test_view/test_view.html', {
            'form': form
        })


class AddFavorite(View):
    pass


def add_favorite(request: HttpRequest, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)
        request.session['favorite_product'] = id
        return redirect(reverse('product-detail', args=[product.slug]))
