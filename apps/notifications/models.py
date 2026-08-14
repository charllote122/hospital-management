from django.db import models
from django.conf import settings
import uuid


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('APPOINTMENT', 'Appointment'),
        ('MEDICAL_RECORD', 'Medical Record'),
        ('BILLING', 'Billing'),
        ('LAB_TEST', 'Lab Test'),
        ('PRESCRIPTION', 'Prescription'),
        ('GENERAL', 'General'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    related_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
