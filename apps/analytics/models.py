from django.db import models
from django.conf import settings

class Analytics(models.Model):
    METRIC_TYPES = (
        ('patient', 'Patient Statistics'),
        ('appointment', 'Appointment Statistics'),
        ('revenue', 'Revenue Statistics'),
        ('inventory', 'Inventory Statistics'),
        ('pharmacy', 'Pharmacy Statistics'),
        ('lab', 'Lab Statistics'),
        ('staff', 'Staff Statistics'),
        ('satisfaction', 'Patient Satisfaction'),
        ('wait_time', 'Wait Time'),
        ('turnover', 'Turnover Rate'),
        ('other', 'Other'),
    )
    
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES, default='other')
    title = models.CharField(max_length=200, default='Analytics Report')
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    previous_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    change_percentage = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)  # This is auto-set on creation
    time_period = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    chart_data = models.JSONField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_analytics')
    
    def __str__(self):
        return f"{self.metric_type} - {self.title} - {self.value}"
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Analytics'
        verbose_name_plural = 'Analytics'
        indexes = [
            models.Index(fields=['metric_type', 'date']),
            models.Index(fields=['-created_at']),
        ]
