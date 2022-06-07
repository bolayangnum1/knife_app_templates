from django.contrib import admin
from .models import Product, Recommendations, Ordering, Contact, NewProduct, FotoProduct


class InlineFotoProduct(admin.TabularInline):
    model = FotoProduct
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineFotoProduct]
    list_display = ['name', 'price', 'are_available']
    list_filter = ['name', 'price', 'are_available']
    search_fields = ['name', 'price', 'are_available']
    fieldsets = (
        ('Описание продукта', {
            'fields': ('name', 'description')
        }),
        ('Характеристика продукта', {
            'fields': ('image', 'price', 'sale', 'are_available', 'amount')
        }),
    )


class OrderingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'region', 'price', 'basket', 'address']
    list_filter = ['full_name', 'phone_number', 'region', 'price', 'basket', 'address']
    search_fields = ['full_name', 'phone_number', 'region', 'price', 'basket', 'address']


admin.site.register(Product, ProductAdmin)
admin.site.register(Recommendations)
admin.site.register(Ordering, OrderingAdmin)
admin.site.register(Contact)
admin.site.register(NewProduct)
