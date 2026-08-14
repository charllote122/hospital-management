from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_type', 'status')
    list_filter = ('status', 'appointment_type', 'appointment_date', 'is_urgent')
    search_fields = ('patient__user__username', 'doctor__user__username', 'reason')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Appointment Details', {
            'fields': ('patient', 'doctor', 'appointment_type', 'status')
        }),
        ('Schedule', {
            'fields': ('appointment_date', 'end_time', 'duration_minutes')
        }),
        ('Information', {
            'fields': ('reason', 'notes', 'medical_notes')
        }),
        ('Status', {
            'fields': ('is_urgent',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_confirmed', 'mark_as_completed', 'mark_as_cancelled']
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} appointments confirmed.')
    mark_as_confirmed.short_description = "Mark as confirmed"
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} appointments completed.')
    mark_as_completed.short_description = "Mark as completed"
    
    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} appointments cancelled.')
    mark_as_cancelled.short_description = "Mark as cancelled"
