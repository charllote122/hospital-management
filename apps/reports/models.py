from django.db import models
from django.conf import settings
import uuid


class Report(models.Model):
    REPORT_TYPES = (
        ('PATIENT', 'Patient Report'),
        ('FINANCIAL', 'Financial Report'),
        ('OPERATIONAL', 'Operational Report'),
        ('STAFF', 'Staff Report'),
        ('INVENTORY', 'Inventory Report'),
    )
    
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('GENERATED', 'Generated'),
        ('REVIEWED', 'Reviewed'),
        ('ARCHIVED', 'Archived'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='reports/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
