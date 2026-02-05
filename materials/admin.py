from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'material_type',
        'subject',
        'study_year',
        'created_at',
    )
    list_filter = ('material_type', 'subject', 'study_year')
    search_fields = ('title', 'author')

