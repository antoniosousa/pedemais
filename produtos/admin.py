from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','description','availability')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'price', 'description', 'category')