from django.contrib import admin
from .models import ClientRequest, Seller

@admin.register(ClientRequest)
class ClientRequestAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'min_price', 'max_price', 'current_date', 'product_type', 'most_views', 'newest', 'top_rated')
    search_fields = ('product_type', 'product_details')
    list_filter = ('current_date', 'product_type', 'most_views', 'newest', 'top_rated')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return '<img src="%s" width="100" height="100" />' % obj.image.url
        return 'No Image'
    
    display_image.allow_tags = True
    display_image.short_description = 'Image'