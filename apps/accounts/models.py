from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    USER_TYPE_CHOICES = (('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient'), ('staff', 'Staff'), ('nurse', 'Nurse'), ('receptionist', 'Receptionist'))
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='patient')
    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
