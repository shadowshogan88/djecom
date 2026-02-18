from django.shortcuts import render
from .models import Category, SubCategory


def home(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    context = {
        'categories': categories,
        'featured_products': []  # Load from database when models are ready
    }
    return render(request, "myapp/home.html", context)


def shop(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    context = {
        'categories': categories,
    }
    return render(request, "myapp/home.html", context)


def category(request, category_id):
    categories = Category.objects.prefetch_related('subcategories').all()
    context = {
        'categories': categories,
    }
    return render(request, "myapp/home.html", context)


def product(request, product_id):
    categories = Category.objects.prefetch_related('subcategories').all()
    context = {
        'categories': categories,
    }
    return render(request, "myapp/home.html", context)
