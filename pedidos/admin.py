from django.contrib import admin
from .models import Pedidos, PedidosItem  # noqa: F401

class PedidosItemInline(admin.TabularInline):
    model = PedidosItem
    extra = 1

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_create', 'total_preco')
    list_filter = ('status',)
    search_fields = ('id',)
    inlines = [PedidosItemInline]
