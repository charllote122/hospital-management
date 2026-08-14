from rest_framework import serializers
from .models import InventoryItem, InventoryLog


class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = ['id', 'item', 'transaction_type', 'quantity', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']


class InventoryItemSerializer(serializers.ModelSerializer):
    logs = InventoryLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'unit', 'location', 'price_per_unit', 'reorder_level', 'logs']
        read_only_fields = ['id']
