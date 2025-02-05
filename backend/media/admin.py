from django.contrib import admin

from media.models import Media

# Register your models here.
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_type', 'variant', 'url', 'created_at')
    search_fields = ('url',)