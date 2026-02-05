from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'material',
        'owner',
        'mode',
        'status',
        'created_at',
    )
    list_filter = ('mode', 'status')
    search_fields = ('material__title', 'owner__username')

