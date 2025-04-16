from add_contact_details import AddDetails

class AddressBookMain:
    
    def __init__(self):
        self.details = []
        
    def __len__(self):
        return len(self.details)
        
    def __iter__(self):
        return iter(self.details)
    
    def add_contact(self):
        detail = AddDetails.add_contact()
        self.details.append(detail)
        print("Details added!!!")
        
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