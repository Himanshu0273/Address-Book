import re
from functools import wraps

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print("THis is kwargs: ", kwargs)
        patterns={
            'first_name': r"^[a-zA-Z]{2,}$",
            'last_name': r"^[a-zA-Z]{2,}$",
            'address': r"^[a-zA-Z0-9\s,.-]+$",
            'city': r"^[a-zA-Z0-9\s,.-]+$",
            'state': r"^[a-zA-Z\s]{1,}$",
            'zip': r"^\d{6}$",
            'phone_number': r"^(\+[0-9]{1,3}\s)?[1-9][0-9]{9}$",
            'email': r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        }
        
        for field, pattern in patterns.items():
            if field in kwargs:
                if not re.fullmatch(pattern, kwargs[field]):
                    raise ValueError(f"Invalid value for {field}: {kwargs[field]}")
        
        return func(*args, **kwargs)
         
    return wrapper
