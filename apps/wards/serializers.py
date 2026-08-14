from rest_framework import serializers
from .models import Ward, Bed


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'ward', 'bed_number', 'status', 'patient']
        read_only_fields = ['id']


class WardSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ward
        fields = ['id', 'name', 'ward_type', 'floor', 'total_beds', 'available_beds', 'description', 'beds']
        read_only_fields = ['id']
