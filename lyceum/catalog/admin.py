from django.contrib import admin

from .models import Category, Item, Photo, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Photo)


class MainPhoto(admin.TabularInline):
    """Class for main photo by item"""

    model = Photo
    extra = 1
    fk_name = 'item_main'
    fields = ('image',)


class GalleryInline(admin.TabularInline):
    """Class for gallery admin panel."""

    model = Photo
    fk_name = 'item_galery'
    fields = ('image',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Class for item admin panel."""

    list_display = (
        'name',
        'is_published',
        'show_image_preview',
    )
    list_editable = ('is_published', )
    list_display_links = ('name', )
    filter_horizontal = ('tags', )
    inlines = (
        MainPhoto,
        GalleryInline,
    )

    def show_image_preview(self, obj):
        """
        :param obj: Item object
        :return: html tag with url to objects photo
        """
        return obj.photo.image_tmb()

    show_image_preview.short_description = 'Изображение'
