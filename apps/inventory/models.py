from django.db import models
from django.conf import settings

class InventoryItem(models.Model):
    CATEGORY_CHOICES = (
        ('medical', 'Medical Supplies'),
        ('equipment', 'Medical Equipment'),
        ('pharmacy', 'Pharmacy'),
        ('office', 'Office Supplies'),
        ('cleaning', 'Cleaning Supplies'),
        ('surgical', 'Surgical Supplies'),
        ('lab', 'Lab Supplies'),
        ('other', 'Other'),
    )
    
    UNIT_CHOICES = (
        ('unit', 'Unit'),
        ('box', 'Box'),
        ('pack', 'Pack'),
        ('bottle', 'Bottle'),
        ('vial', 'Vial'),
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('ml', 'Milliliter'),
        ('mg', 'Milligram'),
        ('g', 'Gram'),
        ('kg', 'Kilogram'),
        ('l', 'Liter'),
        ('pair', 'Pair'),
        ('set', 'Set'),
        ('roll', 'Roll'),
    )
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    min_quantity = models.IntegerField(default=10)
    max_quantity = models.IntegerField(default=100)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='unit')
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    reorder_level = models.IntegerField(default=10)
    location = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    supplier_contact = models.CharField(max_length=100, blank=True, null=True)
    batch_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_inventory_items')
    
    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"
    
    @property
    def stock_status(self):
        if self.quantity <= 0:
            return 'Out of Stock'
        elif self.quantity <= self.reorder_level:
            return 'Low Stock'
        elif self.quantity >= self.max_quantity:
            return 'Overstock'
        else:
            return 'In Stock'
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Inventory Item'
        verbose_name_plural = 'Inventory Items'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
            models.Index(fields=['-created_at']),
        ]

class InventoryLog(models.Model):
    ACTION_CHOICES = (
        ('purchase', 'Purchase'),
        ('usage', 'Usage'),
        ('adjustment', 'Adjustment'),
        ('return', 'Return'),
        ('damage', 'Damage'),
        ('expired', 'Expired'),
        ('restock', 'Restock'),
        ('transfer', 'Transfer'),
        ('received', 'Received'),
    )
    
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    quantity = models.IntegerField()
    previous_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    reference = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='inventory_logs')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.action} - {self.item.name} - {self.quantity} units"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Inventory Log'
        verbose_name_plural = 'Inventory Logs'

class StockAlert(models.Model):
    ALERT_TYPES = (
        ('low', 'Low Stock'),
        ('out', 'Out of Stock'),
        ('expiry', 'Expiry Warning'),
        ('expired', 'Expired'),
        ('overstock', 'Overstock'),
        ('reorder', 'Needs Reorder'),
    )
    
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    resolved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='resolved_alerts')
    
    def __str__(self):
        return f"{self.alert_type} - {self.item.name}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Stock Alert'
        verbose_name_plural = 'Stock Alerts'
