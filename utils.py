"""
Utility Functions for Git Course Application

This module provides common utility functions used across the application.
Functions are organized by category for easy maintenance and testing.
"""

import uuid
import re
from datetime import datetime
from typing import Union


def format_currency(amount: float, currency_symbol: str = "$") -> str:
    """
    Format a number as currency with proper thousands separators.
    
    Args:
        amount: The numeric amount to format
        currency_symbol: The currency symbol to use (default: $)
    
    Returns:
        Formatted currency string
        
    Example:
        >>> format_currency(1234.56)
        '$1,234.56'
    """
    return f"{currency_symbol}{amount:,.2f}"


def validate_age(age: int) -> bool:
    """
    Validate if an age is within reasonable human limits.
    
    Args:
        age: The age to validate
        
    Returns:
        True if age is valid (0-150), False otherwise
    """
    return isinstance(age, int) and 0 <= age <= 150


def generate_unique_id(prefix: str = "") -> str:
    """
    Generate a unique identifier with optional prefix.
    
    Args:
        prefix: Optional prefix for the ID
        
    Returns:
        Unique string identifier
        
    Example:
        >>> generate_unique_id("user")
        'user_a1b2c3d4'
    """
    unique_id = str(uuid.uuid4())[:8]
    return f"{prefix}_{unique_id}" if prefix else unique_id


def format_datetime(date_obj: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format a datetime object as a string.
    
    Args:
        date_obj: The datetime object to format
        format_string: The format string to use
        
    Returns:
        Formatted date string
    """
    return date_obj.strftime(format_string)


def validate_email(email: str) -> bool:
    """
    Validate email address format using regex.
    
    Args:
        email: The email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length with optional suffix.
    
    Args:
        text: The string to truncate
        max_length: Maximum allowed length
        suffix: Suffix to add when truncating
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix