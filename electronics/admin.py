from django.contrib import admin
from django.utils.html import format_html
from .models import Product, TradingNetwork

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_filter = ('name',)

@admin.register(TradingNetwork)
class TradingNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'level', 'email', 'country', 'city', 'get_supplier_link',
        'debt_to_supplier', 'created_at'
    )
    list_filter = ('city',)  # Фильтр по названию города
    actions = ['clear_debt']

    # Метод для создания ссылки на поставщика
    def get_supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/electronics/tradingnetwork/{obj.supplier.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"
    get_supplier_link.short_description = 'Поставщик'

    # Admin Action для очистки задолженности
    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt_to_supplier=0.00)
        self.message_user(request, f'Задолженность очищена для {updated_count} объектов.')
