# import pytest
# from contact_info import Contact
# from  address_book_main import AddressBookMain

# @pytest.fixture
# def fake_contact():
#     contacts = []
#     with open("test_input.txt", "r") as f:
#         lines = f.read().strip().split("\n\n") 
#         for block in lines:
#             parts = block.strip().split("\n")
#             if len(parts) != 8:
#                 continue  
#             contact = Contact(
#                 parts[0],  
#                 parts[1],  
#                 parts[2],  
#                 parts[3],  
#                 parts[4],  
#                 parts[5],  
#                 parts[6],  
#                 parts[7]   
#             )
#             contacts.append(contact)
#     return contacts

# @pytest.fixture

# def add_contacts(fake_contact):
#     book = AddressBookMain()
#     book.details.extend(fake_contact)
#     return book

# def test_contacts(add_contacts):
#     assert len(add_contacts) == 10
#     assert all(isinstance(c,Contact) for c in add_contacts)


import pytest
from address_book_main import AddressBookMain

#Fixture to load the data for testing
@pytest.fixture
def add_contacts():
    book = AddressBookMain()
    with open("test_input.txt","r") as file:
        lines = file.read().strip().split("\n\n")
        for block in lines:
            parts = block.split("\n")
            if len(parts)!=8:
                continue
            contact_kwargs={
                "first_name": parts[0],
                "last_name": parts[1],
                "address": parts[2],
                "city": parts[3],
                "state": parts[4],
                "zip": parts[5],
                "phno": parts[6],
                "email": parts[7]
            }
            book.add_contact(**contact_kwargs)
        return book
    
#test to check if the contacts are being added successfully
def test_add_contact(add_contacts):
    assert len(add_contacts)==10
    

#test to check if the edit function is working properly
