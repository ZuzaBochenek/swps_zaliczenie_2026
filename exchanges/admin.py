from django.contrib import admin
from .models import ExchangeRequest


@admin.register(ExchangeRequest)
class ExchangeRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'listing',
        'requester',
        'status',
        'created_at',
    )
    list_filter = ('status',)
    search_fields = ('listing__material__title', 'requester__username')

