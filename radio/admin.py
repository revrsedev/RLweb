from django.contrib import admin
from .models import Podcast, LiveShow, RadioSettings, BlogPost
from django.utils.html import format_html


admin.site.register(Podcast)

class LiveShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'dj_name', 'live_status', 'start_time', 'end_time')
    list_filter = ('live_status', 'start_time')
    search_fields = ('title', 'dj_name')

admin.site.register(LiveShow, LiveShowAdmin)

@admin.register(RadioSettings)
class RadioSettingsAdmin(admin.ModelAdmin):
    list_display = ['stream_url']
    actions = None  # Disable all admin actions like delete

    def has_add_permission(self, request):
        # Disable add if settings already exist
        return not RadioSettings.objects.exists()

    def has_change_permission(self, request, obj=None):
        # Allow if no object has been created
        return not RadioSettings.objects.exists() or obj is not None

    def has_delete_permission(self, request, obj=None):
        # Disable delete permission
        return False

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'image_display')  # Include image display method
    list_filter = ('publish_date', 'author')
    search_fields = ('title', 'content')

    def image_display(self, obj):
        """image thumbnails"""
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)
        return "No Image"
    image_display.short_description = 'Image Preview'

admin.site.register(BlogPost, BlogPostAdmin)