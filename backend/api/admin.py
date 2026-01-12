from django.contrib import admin
from .models import GrainPrice, ChatMessage

# Customize the admin site headers (optional but nice)
admin.site.site_header = "Grain Price Admin"
admin.site.site_title = "Grain Admin Portal"
admin.site.index_title = "Welcome to Grain Price Management"


@admin.register(GrainPrice)
class GrainPriceAdmin(admin.ModelAdmin):
    """Admin interface for GrainPrice model"""
    
    list_display = ['grain_type', 'price_display', 'date']
    list_filter = ['grain_type', 'date']
    search_fields = ['grain_type']
    ordering = ['-date']
    
    def price_display(self, obj):
        """Format price with dollar sign"""
        return f"${obj.price}"
    price_display.short_description = 'Price (CAD)'


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """Admin interface for ChatMessage model"""
    
    list_display = ['role', 'content_preview', 'created_at']
    list_filter = ['role', 'created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    def content_preview(self, obj):
        """Show first 50 characters of content"""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'