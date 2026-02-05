from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'reviewer',
        'reviewed_user',
        'rating',
        'created_at',
    )
    list_filter = ('rating',)
    search_fields = (
        'reviewer__username',
        'reviewed_user__username',
        'comment',
    )


