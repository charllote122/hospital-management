from django.contrib import admin
from .models import Analytics

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('metric_type', 'title', 'value', 'change_percentage', 'date', 'time_period', 'department')
    list_filter = ('metric_type', 'date', 'time_period', 'department')
    search_fields = ('title', 'description', 'department')
    readonly_fields = ('date', 'created_at', 'updated_at')  # Make date read-only
    
    fieldsets = (
        ('Metric Information', {
            'fields': ('metric_type', 'title', 'description', 'department')
        }),
        ('Values', {
            'fields': ('value', 'previous_value', 'change_percentage')
        }),
        ('Data', {
            'fields': ('chart_data', 'time_period')  # Removed date from here
        }),
        ('Additional', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('date', 'created_at', 'updated_at', 'created_by'),
            'classes': ('collapse',),
        }),
    )
    
    # Auto-set date when saving
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new
            from django.utils import timezone
            obj.date = timezone.now().date()
        super().save_model(request, obj, form, change)
