from django.contrib import admin
from .models import Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'specialization', 'department', 'is_available')
    list_filter = ('specialization', 'department', 'is_available')
    search_fields = ('user__username', 'user__email', 'specialization')
    def is_available(self, obj):
        return obj.available if hasattr(obj, 'available') else True
    is_available.boolean = True
    is_available.short_description = 'Available'
