from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'listing',
        'reviewer',
        'rating',
        'created_at',
    )
    list_filter = ('rating',)
    search_fields = ('listing__material__title', 'reviewer__username')

