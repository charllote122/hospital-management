from django.contrib import admin
from .models import MedicalRecord, Diagnosis, LabResult, MedicalPrescription

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'title', 'record_type', 'doctor', 'created_at')
    list_filter = ('record_type', 'created_at')
    search_fields = ('patient__user__username', 'title', 'description')

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'icd10_code', 'doctor', 'date')
    list_filter = ('date', 'is_active')
    search_fields = ('patient__user__username', 'diagnosis', 'icd10_code')

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'test_date', 'is_abnormal', 'doctor')
    list_filter = ('test_date', 'is_abnormal')
    search_fields = ('patient__user__username', 'test_name')

@admin.register(MedicalPrescription)
class MedicalPrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'dosage', 'doctor', 'prescribed_date', 'is_active')
    list_filter = ('is_active', 'prescribed_date')
    search_fields = ('patient__user__username', 'medication')
