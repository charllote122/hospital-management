from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['staff', 'shift', 'date', 'start_time', 'end_time']
    list_filter = ['shift', 'date', 'created_at']
    search_fields = ['staff__first_name', 'staff__last_name']
    readonly_fields = ['id', 'created_at', 'updated_at']
