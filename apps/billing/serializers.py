from rest_framework import serializers
from .models import Bill, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'bill', 'amount', 'payment_method', 'payment_date', 'transaction_id']
        read_only_fields = ['id', 'payment_date']


class BillSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bill
        fields = ['id', 'patient', 'appointment', 'amount', 'status', 'description', 'issued_date', 'due_date', 'paid_date', 'payments']
        read_only_fields = ['id', 'issued_date']
