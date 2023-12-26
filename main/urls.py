from django.urls import path
from main.views import index, contacts, category, products, product
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/product/', product, name='product')
]
