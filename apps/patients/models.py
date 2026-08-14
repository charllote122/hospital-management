from django.db import models
from django.conf import settings
import uuid


class Patient(models.Model):
    BLOOD_TYPES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    MARITAL_STATUS = (
        ("SINGLE", "Single"),
        ("MARRIED", "Married"),
        ("DIVORCED", "Divorced"),
        ("WIDOWED", "Widowed"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile",
    )
    patient_id = models.CharField(max_length=20, unique=True)
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_TYPES, blank=True, null=True
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS, default="SINGLE"
    )
    occupation = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    allergies = models.JSONField(default=list, blank=True)
    chronic_conditions = models.JSONField(default=list, blank=True)
    medications = models.JSONField(default=list, blank=True)
    emergency_contact = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relation = models.CharField(max_length=50)
    medical_history = models.TextField(blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    insurance_number = models.CharField(max_length=50, blank=True, null=True)
    primary_care_physician = models.ForeignKey(
        "doctors.Doctor", on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "patients"
        indexes = [
            models.Index(fields=["patient_id"]),
            models.Index(fields=["blood_group"]),
        ]

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.patient_id}"

    def save(self, *args, **kwargs):
        if not self.patient_id:
            import random

            self.patient_id = f"PAT-{random.randint(100000, 999999)}"
        super().save(*args, **kwargs)
