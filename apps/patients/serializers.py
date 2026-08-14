from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'user', 'blood_group', 'gender', 'marital_status', 'occupation', 'nationality', 'allergies', 'chronic_conditions', 'medications', 'emergency_contact']
        read_only_fields = ['id']


class PatientDetailSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'user', 'user_details', 'blood_group', 'gender', 'marital_status', 'occupation', 'nationality', 'allergies', 'chronic_conditions', 'medications', 'emergency_contact']
        read_only_fields = ['id']
    
    def get_user_details(self, obj):
        return {
            'id': str(obj.user.id),
            'username': obj.user.username,
            'email': obj.user.email,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
        }
