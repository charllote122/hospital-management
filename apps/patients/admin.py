from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'get_name', 'blood_group', 'gender', 'emergency_contact']
    list_filter = ['blood_group', 'gender', 'marital_status']
    search_fields = ['patient_id', 'user__username', 'user__email']
    readonly_fields = ['id']
    fieldsets = (
        ('Personal Info', {'fields': ('id', 'user', 'patient_id', 'gender', 'blood_group')}),
        ('Contact & Status', {'fields': ('marital_status', 'emergency_contact')}),
        ('Additional Info', {'fields': ('occupation', 'nationality', 'allergies', 'chronic_conditions', 'medications')}),
    )
    
    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_name.short_description = 'Name'
