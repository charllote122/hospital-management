"""
Exception classes for the hospital management system.
"""

from rest_framework.exceptions import APIException


class HospitalManagementException(APIException):
    """Base exception for hospital management system"""
    status_code = 400
    default_detail = 'An error occurred in the hospital management system.'


class PatientNotFound(HospitalManagementException):
    """Exception when patient is not found"""
    status_code = 404
    default_detail = 'Patient not found.'


class AppointmentConflict(HospitalManagementException):
    """Exception when appointment times conflict"""
    status_code = 409
    default_detail = 'Appointment time conflicts with existing appointment.'


class InsufficientInventory(HospitalManagementException):
    """Exception when inventory is insufficient"""
    status_code = 400
    default_detail = 'Insufficient inventory.'


class UnauthorizedAccess(HospitalManagementException):
    """Exception for unauthorized access"""
    status_code = 403
    default_detail = 'You do not have permission to access this resource.'
