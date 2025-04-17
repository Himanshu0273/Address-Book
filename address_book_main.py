# from add_contact_details import AddDetails
from contact_info import Contact
import re

#Decoratoe to validate input that the user enters:
def validate_input(func):
    def wrapper(*args, **kwargs):
        fn_pattern=r"^[A-Z][a-z]{2,}$"
        ln_pattern=r"^[A-Z][a-z]{2,}$"
        address_pattern=r"^[A-Za-z0-9\s,.-]+$"
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
    def edit_details(self, first_name, last_name):
        contact=None
        for c in self.details:
            if c.first_name == first_name and c.last_name == last_name:
                contact=c
                break
            
        if contact:
            print("Contact Found!!")
            print(contact)
            while True:
                print("""Choose an option to edit a detail:
                        1. Enter 1 to edit First Name.
                        2. Enter 2 to edit Last Name.
                        3. Enter 3 to edit Address.
                        4. Enter 4 to edit City.
                        5. Enter 5 to edit State.
                        6. Enter 6 to edit Zip.
                        7. Enter 7 to edit Phone number.
                        8. Enter 8 to edit Email ID.
                        0. Enter 0 to exit                    
                    """)
                choice=input("Enter your choice: ")
                match(choice):
                    case "1":
                        new_first_name = input("Enter the new first name: ")
                        contact.first_name = new_first_name
                    
                    case "2":
                        new_last_name = input("Enter the new last name: ")
                        contact.last_name = new_last_name
                        
                    case "3":
                        new_address = input("Enter new address: ")
                        contact.address = new_address
                    
                    case "4":
                        new_city = input("Enter new city: ")
                        contact.city = new_city
                    
                    case "5":
                        new_state = input("Enter new state: ")
                        contact.state = new_state
                    
                    case "6":
                        new_zip = input("Enter new zip code: ")
                        contact.zip = new_zip
                        
                    case "7":
                        new_phno = input("Enter new phone number: ")
                        contact.phno = new_phno
                    
                    case "8":
                        new_email = input("Enter new email ID: ")
                        contact.email = new_email
                    
                    case "0":
                        print("Editing Complete!!")
                        break
        else:
            print("No contact found.Try again!!!")    
    
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