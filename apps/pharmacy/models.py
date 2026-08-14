from django.db import models
from django.conf import settings
from apps.patients.models import Patient
from apps.doctors.models import Doctor

class Medicine(models.Model):
    CATEGORY_CHOICES = (
        ('antibiotic', 'Antibiotic'),
        ('analgesic', 'Analgesic'),
        ('antidepressant', 'Antidepressant'),
        ('antihistamine', 'Antihistamine'),
        ('antiviral', 'Antiviral'),
        ('painkiller', 'Painkiller'),
        ('vitamin', 'Vitamin'),
        ('supplement', 'Supplement'),
        ('other', 'Other'),
    )
    
    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    manufacturer = models.CharField(max_length=200)
    dosage_form = models.CharField(max_length=50)
    strength = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.strength})"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Medicines'

class PharmacyPrescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pharmacy_prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='pharmacy_prescriptions')
    medication = models.CharField(max_length=200)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    instructions = models.TextField()
    refills = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    prescribed_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient} - {self.medication} - {self.dosage}"
    
    class Meta:
        ordering = ['-prescribed_date']
        verbose_name = 'Pharmacy Prescription'
        verbose_name_plural = 'Pharmacy Prescriptions'
