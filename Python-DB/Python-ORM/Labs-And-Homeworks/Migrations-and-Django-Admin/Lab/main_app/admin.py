from django.contrib import admin

from models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_on')
    search_fields = ('name', 'category', 'supplier')
    list_filter = ('category', 'supplier')
    date_hierarchy = 'created_on'

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'price', 'barcode')
        }),
        ('Categorization', {
            'fields': ('category', 'supplier')
        }),
    )