from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    staff_name = serializers.CharField(source='staff.get_full_name', read_only=True)
    
    class Meta:
        model = Schedule
        fields = ['id', 'staff', 'staff_name', 'shift', 'date', 'start_time', 'end_time', 'notes']
        read_only_fields = ['id']
