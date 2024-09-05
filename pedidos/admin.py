from django.contrib import admin
from .models import Order, OrderedItem

class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_create', 'total_price')
    list_filter = ('status',)
    search_fields = ('id',)
    inlines = [OrderedItemInline]

admin.site.register(Order, OrderAdmin)