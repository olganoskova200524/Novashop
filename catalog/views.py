from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    """Главная страница: список товаров"""
    products = Product.objects.select_related('category').all()
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail(request, pk: int):
    """Детальная страница товара"""
    product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def contacts(request):
    """Страница контактов"""
    return render(request, 'catalog/contacts.html')
