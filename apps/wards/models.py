from django.db import models
import uuid


class Ward(models.Model):
    WARD_TYPES = (
        ('GENERAL', 'General'),
        ('ICU', 'Intensive Care Unit'),
        ('PEDIATRICS', 'Pediatrics'),
        ('MATERNITY', 'Maternity'),
        ('SURGERY', 'Surgery'),
        ('ISOLATION', 'Isolation'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    ward_type = models.CharField(max_length=50, choices=WARD_TYPES)
    floor = models.IntegerField()
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['floor', 'name']
    
    def __str__(self):
        return f"{self.name} - Floor {self.floor}"


class Bed(models.Model):
    BED_STATUS = (
        ('AVAILABLE', 'Available'),
        ('OCCUPIED', 'Occupied'),
        ('MAINTENANCE', 'Maintenance'),
        ('RESERVED', 'Reserved'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=BED_STATUS, default='AVAILABLE')
    patient = models.OneToOneField('patients.Patient', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_assignment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['ward', 'bed_number']
        ordering = ['ward', 'bed_number']
    
    def __str__(self):
        return f"{self.ward.name} - Bed {self.bed_number}"
