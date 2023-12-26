from django.shortcuts import render
from main.models import Category, Product


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', context)


def category(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'main/category.html', context)


def products(request, pk):
    category_name = Category.objects.get(pk=pk)
    context = {
        'objects_list': Product.objects.filter(category=pk),
        'title': category_name
    }
    return render(request, 'main/products.html', context)


def product(request, pk):
    context = {
        'objects_list': Product.objects.get(pk=pk),
        'title': 'Товар'
    }
    return render(request, 'main/product.html', context)
