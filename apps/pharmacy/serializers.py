from rest_framework import serializers
from .models import Medicine, Prescription


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'manufacturer', 'expiry_date']
        read_only_fields = ['id']


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'doctor', 'medicine', 'dosage', 'frequency', 'duration_days', 'quantity', 'issued_date', 'notes']
        read_only_fields = ['id', 'issued_date']
