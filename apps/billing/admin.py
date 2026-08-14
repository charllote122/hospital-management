from django.contrib import admin
from .models import Invoice, InvoiceItem, Payment

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'patient', 'total', 'status', 'issue_date', 'due_date')
    list_filter = ('status', 'payment_method', 'issue_date')
    search_fields = ('invoice_number', 'patient__user__username', 'patient__user__email')
    readonly_fields = ('subtotal', 'tax', 'discount', 'total', 'amount_paid', 'balance')
    fieldsets = (
        ('Invoice Information', {
            'fields': ('invoice_number', 'patient', 'doctor')
        }),
        ('Financial', {
            'fields': ('subtotal', 'tax', 'discount', 'total', 'amount_paid', 'balance')
        }),
        ('Payment', {
            'fields': ('status', 'payment_method', 'due_date')
        }),
        ('Additional', {
            'fields': ('notes', 'created_by')
        }),
    )

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'total')
    search_fields = ('description', 'invoice__invoice_number')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'patient', 'amount', 'payment_method', 'status', 'payment_date')
    list_filter = ('status', 'payment_method', 'payment_date')
    search_fields = ('transaction_id', 'invoice__invoice_number', 'patient__user__username')
