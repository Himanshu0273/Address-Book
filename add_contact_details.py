from contact_info import Contact
import re

class AddDetails:
    
    @staticmethod
    def validate(detail, pattern, error_text):
        while True:
            value = input(detail)
            if re.match(pattern, value):
                return value
            else:
                print(error_text)
                
    @staticmethod
    def add_contact():
        print("Add your contact details here: ")
        first_name = AddDetails.validate("First Name: ", r"^[A-Z][a-z]{2,}$", "Invalid First Name")
        last_name = AddDetails.validate("Last Name: ", r"^[A-Z][a-z]{2,}$", "Invalid Last Name")
        address = AddDetails.validate("Address: ", r"^[A-Z][a-zA-Z\s]{1,}$", "Invalid Address")
        city = AddDetails.validate("City: ", r"^[A-Z][a-zA-Z\s]{1,}$", "Invalid City")
        state = AddDetails.validate("State: ", r"^[A-Z][a-zA-Z\s]{1,}$", "Invalid State")
        zip = AddDetails.validate("Zip Code: ", r"^\d{6}$", "Invalid Zip Code")
        phno = AddDetails.validate("Phone Number: ", r"^\+[0-9]{1,3} [1-9][0-9]{9}$", "Invalid Phone Number")
        email = AddDetails.validate("Email Id: ", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Invalid Email Id")
        
        return Contact(first_name, last_name, address, city, state, zip, phno, email)