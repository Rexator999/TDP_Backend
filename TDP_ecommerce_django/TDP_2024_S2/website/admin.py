from django.contrib import admin
from .models import ClientRequest, SellerProduct, Client, Seller

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

@admin.register(ClientRequest)
class ClientRequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'client', 'min_price', 'max_price', 'request_date', 'end_date', 'product_type', 'product_con')
    search_fields = ('product_type', 'product_details')
    list_filter = ('request_date', 'product_type', 'product_con')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

@admin.register(SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'seller', 'display_image', 'key_words')

    def display_image(self, obj):
        if obj.image:
            return '<img src="%s" width="100" height="100" />' % obj.image.url
        return 'No Image'
    
    display_image.allow_tags = True
    display_image.short_description = 'Image'