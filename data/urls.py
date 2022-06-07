from django.urls import path
from data import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='product_list'),
    path('', views.RecommendationsView.as_view(), name='collection_list'),
    path('new-product/', views.NewProduct.as_view(), name='new_product.html'),
]
