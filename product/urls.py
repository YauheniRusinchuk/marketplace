from django.urls import path
from product.views import add_product

app_name = 'products'

urlpatterns = [
    path('', add_product, name='products_index'),
]
