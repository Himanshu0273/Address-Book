class Contact:
    
    def __init__(self, first_name, last_name, address, city, state, zip, phno, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phno = phno
        self.email = email
        
    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Address: {self.address}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip Code: {self.zip}\n"
            f"Phone Number: {self.phno}\n"
            f"Email ID: {self.email}"            
        )    
        
# print(Contact("Himanshu", "Baid", "Ideal Grand", "Howrah", "West Bengal", 711102, 8910322481, "abc@gmail.com"))