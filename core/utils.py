"""
Utility functions for the hospital management system.
"""

from django.shortcuts import get_object_or_404


def get_object_or_none(model, **kwargs):
    """
    Get object from model or return None if not found.
    """
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def validate_user_role(user, required_role):
    """
    Validate if user has the required role.
    """
    if not user.is_authenticated:
        return False
    return getattr(user, 'role', None) == required_role


def calculate_age(birth_date):
    """
    Calculate age from birth date.
    """
    from datetime import date
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
