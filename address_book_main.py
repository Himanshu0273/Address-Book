# from add_contact_details import AddDetails
from contact_info import Contact
from Schema.schema import ContactSchema, create_contact

class AddressBookMain:
    
    def __init__(self):
        self.details = []
        
    def __len__(self):
        return len(self.details)
        
    def __iter__(self):
        return iter(self.details)
    
    #Add Details 
    def add_contact(self,**kwargs):
        try:
            contact_data=create_contact(**kwargs)
            detail=Contact(
                contact_data.first_name,
                contact_data.last_name,
                contact_data.address,
                contact_data.city,
                contact_data.state,
                contact_data.zip,
                contact_data.phone_number,
                contact_data.email
            )
            self.details.append(detail)
            print("Details Added")
        except ValueError as e:
            print(f"Error occured: {e}")
        
    #Edit Details
    def edit_details(self, first_name, last_name):
        contact=None
        for c in self.details:
            if c.first_name.lower() == first_name.lower():
                if c.last_name.lower() == last_name.lower():
                    contact=c
                    break
        else:
            print("Contact not present")
            
        
        if contact:
            print("Contact Found!!")
            print(contact)
            while True:
                print("""
Choose an option to edit a detail:

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
                        new_first_name = input("Enter the new first name: ").strip()
                        contact.first_name = new_first_name
                    
                    case "2":
                        new_last_name = input("Enter the new last name: ").strip()
                        contact.last_name = new_last_name
                        
                    case "3":
                        new_address = input("Enter new address: ").strip()
                        contact.address = new_address
                    
                    case "4":
                        new_city = input("Enter new city: ").strip()
                        contact.city = new_city
                    
                    case "5":
                        new_state = input("Enter new state: ").strip()
                        contact.state = new_state
                    
                    case "6":
                        new_zip = input("Enter new zip code: ").strip()
                        contact.zip = new_zip
                        
                    case "7":
                        new_phone_number = input("Enter new phone number: ").strip()
                        contact.phone_number = new_phone_number
                    
                    case "8":
                        new_email = input("Enter new email ID: ").strip()
                        contact.email = new_email
                    
                    case "0":
                        print("Editing Complete!!")
                        break
                print()
                print ("Updated Contact: ")
                print(contact)
          

    #Delete Details
    def delete_details(self, first_name, last_name):
        contact = None
        for c in self.details:
            if c.first_name.lower() == first_name.lower() and c.last_name.lower() == last_name.lower():
                self.details.remove(c)
                print (f"Contact info of: {first_name} {last_name} is removed!!!")
                break
        else:
            print("No contact found!!")
        
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