import re
from functools import wraps

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print("THis is kwargs: ", kwargs)
        patterns={
            'first_name': r"^[A-Z][a-z]{2,}$",
            'last_name': r"^[A-Z][a-z]{2,}$",
            'address': r"^[A-Za-z0-9\s,.-]+$",
            'city': r"^[A-Za-z0-9\s,.-]+$",
            'state': r"^[A-Z][a-zA-Z\s]{1,}$",
            'zip': r"^\d{6}$",
            'phno': r"^(\+[0-9]{1,3}\s)?[1-9][0-9]{9}$",
            'email': r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        }
        
        for field, pattern in patterns.items():
            if field in kwargs:
                if not re.match(pattern, kwargs[field]):
                    raise ValueError(f"Invalid {field.replace('_', ' ').title()}!!")
                
        return func(*args, **kwargs)
    
    return wrapper