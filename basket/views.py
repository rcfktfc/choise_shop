from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Basket
from main.models import Product


@login_required
def add_to_basket(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        # Проверяем, есть ли уже этот товар в корзине пользователя
        basket_item, created = Basket.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            basket_item.quantity += 1
            basket_item.save()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'Товар добавлен в корзину',
                'basket_count': Basket.objects.filter(user=request.user).count()
            })

        return redirect('main:product_list')

    return redirect('main:product_list')


@login_required
def basket_view(request):
    basket_items = Basket.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in basket_items)

    return render(request, 'basket/basket.html', {
        'basket_items': basket_items,
        'total_price': total_price
    })


@login_required
def remove_from_basket(request, basket_id):
    if request.method == 'POST':
        basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
        basket_item.delete()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})

        return redirect('basket:basket_view')

    return redirect('basket:basket_view')