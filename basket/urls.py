from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('', views.basket_view, name='basket_view'),
    path('remove/<int:basket_id>/', views.remove_from_basket, name='remove_from_basket'),
]