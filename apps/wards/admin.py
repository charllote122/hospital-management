from django.contrib import admin
from .models import Ward, Bed


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['name', 'ward_type', 'floor', 'total_beds', 'available_beds']
    list_filter = ['ward_type', 'floor']
    search_fields = ['name']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['ward', 'bed_number', 'status', 'patient']
    list_filter = ['ward', 'status']
    search_fields = ['bed_number', 'patient__patient_id']
    readonly_fields = ['id', 'created_at', 'updated_at']
