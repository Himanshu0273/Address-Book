from pydantic import BaseModel, EmailStr
from Utils.validate_input import validate_input

class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip: str
    phno: str
    email: str
    
    @validate_input
    def __init__(self, **kwargs):
        super().__init__(**kwargs)