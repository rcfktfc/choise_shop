# main/admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'is_active') # Отображаемые поля в списке
    list_editable = ('price', 'is_active') # Поля, которые можно редактировать прямо в списке
    search_fields = ('name', 'description') # Поля, по которым работает поиск
    list_filter = ('created_at', 'is_active') # Фильтры сбоку
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Цена и изображение', {'fields': ['price', 'image']}),
        ('Статус', {'fields': ['is_active']}),
    ]

admin.site.register(Product, ProductAdmin)
