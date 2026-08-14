from django.db import models
from django.conf import settings
import uuid


class Schedule(models.Model):
    SHIFT_CHOICES = (
        ('MORNING', 'Morning (6 AM - 2 PM)'),
        ('AFTERNOON', 'Afternoon (2 PM - 10 PM)'),
        ('NIGHT', 'Night (10 PM - 6 AM)'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='schedules')
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date', 'shift']
        unique_together = ['staff', 'date', 'shift']
    
    def __str__(self):
        return f"{self.staff.get_full_name()} - {self.date} ({self.shift})"
