from django.core.mail import BadHeaderError, send_mail
from django.views import View
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from data.models import Product, Recommendations, NewProduct


class ProductView(ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    template_name = 'data/product_list.html'


class RecommendationsView(ListView):
    model = Recommendations
    queryset = Recommendations.objects.all()
    template_name = 'data/collection_list.html'


class NewProduct(ListView):
    model = NewProduct
    queryset = NewProduct.objects.all()
    template_name = 'data/index.html'
