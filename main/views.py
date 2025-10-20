from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required


def index(request):
    # Получаем только активные товары, отсортированные по дате создания (новые сначала)
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'main/index.html', {'products': products})