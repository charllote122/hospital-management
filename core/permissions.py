"""
Django REST Framework utilities and helpers for the hospital management system.
"""

from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    """Permission class to check if user is a doctor"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'DOCTOR'


class IsPatient(BasePermission):
    """Permission class to check if user is a patient"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'PATIENT'


class IsStaff(BasePermission):
    """Permission class to check if user is staff"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'STAFF'


class IsPharmacist(BasePermission):
    """Permission class to check if user is a pharmacist"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'PHARMACIST'


class IsLabTechnician(BasePermission):
    """Permission class to check if user is a lab technician"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'role', None) == 'LAB_TECHNICIAN'
