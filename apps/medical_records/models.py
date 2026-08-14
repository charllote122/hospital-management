from django.db import models
from django.conf import settings
from apps.patients.models import Patient
from apps.doctors.models import Doctor

class MedicalRecord(models.Model):
    RECORD_TYPES = (
        ('consultation', 'Consultation'),
        ('diagnosis', 'Diagnosis'),
        ('treatment', 'Treatment'),
        ('surgery', 'Surgery'),
        ('lab_result', 'Lab Result'),
        ('imaging', 'Imaging'),
        ('prescription', 'Prescription'),
        ('vaccination', 'Vaccination'),
        ('emergency', 'Emergency'),
        ('discharge', 'Discharge'),
        ('other', 'Other'),
    )
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='medical_records')
    # Removed appointment dependency
    record_type = models.CharField(max_length=50, choices=RECORD_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='medical_records/', blank=True, null=True)
    is_confidential = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_medical_records')
    
    def __str__(self):
        return f"{self.patient} - {self.title} ({self.record_type})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnoses')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='diagnoses')
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='diagnoses', blank=True, null=True)
    icd10_code = models.CharField(max_length=20)
    diagnosis = models.TextField()
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient} - {self.diagnosis[:50]}"
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'
        indexes = [
            models.Index(fields=['patient', 'date']),
            models.Index(fields=['icd10_code']),
        ]

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_results')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='lab_results')
    test_name = models.CharField(max_length=200)
    test_date = models.DateField()
    result = models.TextField()
    normal_range = models.CharField(max_length=100, blank=True, null=True)
    is_abnormal = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='lab_results/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient} - {self.test_name} - {self.test_date}"
    
    class Meta:
        ordering = ['-test_date']
        verbose_name = 'Lab Result'
        verbose_name_plural = 'Lab Results'

class MedicalPrescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_prescriptions')
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_prescriptions')
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
        verbose_name = 'Medical Prescription'
        verbose_name_plural = 'Medical Prescriptions'
