from django.contrib import admin
from django.utils.html import format_html
from .models import InventoryItem, InventoryLog, StockAlert

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'stock_status_display', 'reorder_level', 'unit_price')
    list_filter = ('category', 'is_active', 'unit')
    search_fields = ('name', 'description', 'supplier', 'batch_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Stock Management', {
            'fields': ('quantity', 'min_quantity', 'max_quantity', 'unit', 'reorder_level')
        }),
        ('Pricing', {
            'fields': ('unit_price',)
        }),
        ('Supplier Information', {
            'fields': ('supplier', 'supplier_contact', 'batch_number')
        }),
        ('Storage', {
            'fields': ('location', 'expiry_date')
        }),
        ('Status', {
            'fields': ('is_active', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by'),
            'classes': ('collapse',)
        }),
    )
    
    def stock_status_display(self, obj):
        status = obj.stock_status
        colors = {
            'Out of Stock': 'red',
            'Low Stock': 'orange',
            'In Stock': 'green',
            'Overstock': 'blue'
        }
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            colors.get(status, 'black'),
            status
        )
    stock_status_display.short_description = 'Stock Status'

@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'action', 'quantity', 'previous_quantity', 'new_quantity', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('item__name', 'reference', 'notes')
    readonly_fields = ('created_at',)

@admin.register(StockAlert)
class StockAlertAdmin(admin.ModelAdmin):
    list_display = ('item', 'alert_type', 'message', 'is_read', 'resolved', 'created_at')
    list_filter = ('alert_type', 'is_read', 'resolved')
    search_fields = ('item__name', 'message')
