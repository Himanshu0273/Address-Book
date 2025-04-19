class Contact:
    
    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)
        
    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Address: {self.address}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip Code: {self.zip}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Email ID: {self.email}"            
        )    
        
        
    #Check for duplicates
    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.first_name==other.first_name and self.last_name == other.last_name
        return False
# print(Contact("Himanshu", "Baid", "Ideal Grand", "Howrah", "West Bengal", 711102, 8910322481, "abc@gmail.com"))
