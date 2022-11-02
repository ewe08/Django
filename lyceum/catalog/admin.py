from django.contrib import admin
from .models import Item, Category, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_editable = ['is_published']
    filter_horizontal = ['tags']


admin.site.register(Category)
admin.site.register(Tag)
