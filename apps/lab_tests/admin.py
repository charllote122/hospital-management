from django.contrib import admin
from .models import LabTest


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'patient', 'status', 'ordered_date']
    list_filter = ['status', 'ordered_date']
    search_fields = ['test_name', 'patient__patient_id']
    readonly_fields = ['id', 'ordered_date']
