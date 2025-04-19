# import pytest
# from address_book_main import AddressBook

# #Fixture to load the data for testing
# @pytest.fixture
# def add_contacts():
#     book = AddressBook()
#     with open("test_input.txt","r") as file:
#         lines = file.read().strip().split("\n\n")
#         for block in lines:
#             parts = block.split("\n")
#             if len(parts)!=8:
#                 continue
#             contact_kwargs={
#                 "first_name": parts[0],
#                 "last_name": parts[1],
#                 "address": parts[2],
#                 "city": parts[3],
#                 "state": parts[4],
#                 "zip": parts[5],
#                 "phno": parts[6],
#                 "email": parts[7]
#             }
#             book.add_contact(**contact_kwargs)
#         return book
    
# #test to check if the contacts are being added successfully
# def test_add_contact(add_contacts):
#     assert len(add_contacts)==10
    

# #test to check if the edit function is working properly
# # @pytest.mark.parametrize((""))
# def test_edit_details():
#     pass

def test_add_contacts(address_book_with_four_contacts):
    book = address_book_with_four_contacts

    assert len(book.details) == 4

    names = {(c.first_name, c.last_name) for c in book.details}
    expected_names = {
        ("Himanshu", "Baid"),
        ("Kamal", "Baid"),
        ("Gaurav", "Agarwal"),
        ("Krish", "Jain")
    }

    assert names == expected_names
