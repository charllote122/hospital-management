from rest_framework import serializers
from .models import LabTest


class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = ['id', 'patient', 'test_name', 'description', 'status', 'ordered_date', 'completed_date', 'result', 'notes']
        read_only_fields = ['id', 'ordered_date']
