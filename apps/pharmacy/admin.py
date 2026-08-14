from django.contrib import admin
from .models import Medicine, PharmacyPrescription

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock_quantity', 'unit_price', 'expiry_date', 'is_active')
    list_filter = ('category', 'is_active', 'expiry_date')
    search_fields = ('name', 'generic_name', 'manufacturer')

@admin.register(PharmacyPrescription)
class PharmacyPrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'dosage', 'doctor', 'prescribed_date', 'is_active')
    list_filter = ('is_active', 'prescribed_date')
    search_fields = ('patient__user__username', 'medication')
