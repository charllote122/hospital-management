from rest_framework import serializers
from .models import Analytics


class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['id', 'metric_type', 'date', 'value', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
