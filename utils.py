"""
Temporary utility functions - should be moved to proper module
"""

def format_currency(amount):
    return f"${amount:,.2f}"

def validate_age(age):
    return 0 <= age <= 150

def generate_id():
    import uuid
    return str(uuid.uuid4())[:8]

# Quick fix for date formatting
def format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")