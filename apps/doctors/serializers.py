from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'license_number', 'specialization', 'experience_years', 'consultation_fee', 'available']
        read_only_fields = ['id']
    
    def get_user(self, obj):
        return {
            'id': str(obj.user.id),
            'username': obj.user.username,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
            'email': obj.user.email,
        }
