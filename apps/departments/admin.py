from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'floor', 'head', 'phone', 'is_active')
    list_filter = ('is_active', 'floor')
    search_fields = ('name', 'code', 'description', 'head', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'code', 'description')
        }),
        ('Contact & Location', {
            'fields': ('floor', 'phone', 'head')
        }),
        ('Status', {
            'fields': ('is_active', 'established_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
