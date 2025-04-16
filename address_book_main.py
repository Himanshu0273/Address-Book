# from add_contact_details import AddDetails
from contact_info import Contact
import re

def validate_input(func):
    def wrapper(*args, **kwargs):
        fn_pattern=r"^[A-Z][a-z]{2,}$"
        ln_pattern=r"^[A-Z][a-z]{2,}$"
        address_pattern=r"^[A-Z][a-zA-Z\s]{1,}$"
        city_pattern=r"^[A-Z][a-zA-Z\s]{1,}$"
        state_pattern=r"^[A-Z][a-zA-Z\s]{1,}$"
        zip_pattern=r"^\d{6}$"
        phno_pattern=r"^(\+[0-9]{1,3}\s)?[1-9][0-9]{9}$"
        email_pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(fn_pattern,kwargs['first_name']):
            raise ValueError("\nInvalid First Name!!")
        
        if not re.match(ln_pattern, kwargs['last_name']):
            raise ValueError("Invalid !!")
        if not re.match(address_pattern, kwargs['address']):
            raise ValueError("Invalid Address!!")
        
        if not re.match(city_pattern, kwargs['city']):
            raise ValueError("Invalid City!!")
        
        if not re.match(state_pattern, kwargs['state']):
            raise ValueError("Invalid State!!")
        
        if not re.match(zip_pattern, kwargs['zip']):
            raise ValueError("Invalid ZIP Code!!")
        
        if not re.match(phno_pattern, kwargs['phno']):
            raise ValueError("Invalid Phone Number!!")
        
        if not re.match(email_pattern, kwargs['email']):
            raise ValueError("Invalid Email ID!!")
        
        return func(*args, **kwargs)
    return wrapper

class AddressBookMain:
    
    def __init__(self):
        self.details = []
        
    def __len__(self):
        return len(self.details)
        
    def __iter__(self):
        return iter(self.details)
    
    #Add Details
    @validate_input
    def add_contact(self,**kwargs):
        detail =Contact(
            kwargs["first_name"],
            kwargs["last_name"],
            kwargs["address"],
            kwargs["city"],
            kwargs["state"],
            kwargs["zip"],
            kwargs["phno"],
            kwargs["email"]
        )
        self.details.append(detail)
        print("Details added!!!")
        
    #Edit Details
    def edit_details(self):
        pass
    def display_details(self):
        if len(self.details)==0:
            print("Empty Address Book!!!")
            return
        
        print("Contacts: ")
        for i, detail in enumerate(self.details,1):
            print(f"\nContact {i}:\n{detail}")
            
            
# ob1 = AddressBookMain()
# ob1.add_contact()
# ob1.display_details()