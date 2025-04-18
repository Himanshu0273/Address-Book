from pydantic import BaseModel, EmailStr
from Utils.validate_input import validate_input
from typing import get_type_hints

class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip: str
    phone_number: str
    email: str
    

    
@validate_input
def create_contact(**kwargs)->ContactSchema:
    return ContactSchema(**kwargs)

# input details
def contact_details():
    input_data={}
    for field in get_type_hints(ContactSchema).keys():
        value = input(f"{field.replace('_', ' ').title()}: ").strip()
        input_data[field] = value
        
        
    try:
        return create_contact(**input_data)
    except ValueError as e:
        print(f"Validation Error: {e}")
        return None