from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    fieldsets = UserAdmin.fieldsets + (('Additional Info', {'fields': ('phone_number', 'address', 'date_of_birth', 'user_type', 'is_doctor', 'is_patient', 'is_staff_member')}),)
