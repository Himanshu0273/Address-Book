import pytest
from address_book_main import AddressBook
from address_book_system import AddressBookMain
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

#Test edit contact function
# def test_edit_details(address_book_with_four_contacts):
#     pass

#Test the delete contact functionality
def test_delete_contact(address_book_with_four_contacts):
    book = address_book_with_four_contacts
    assert len(book)==4
    
    book.delete_details("Gaurav", "Agarwal")
    rem_names = {(c.first_name, c.last_name) for c in book.details}
    assert {"Gaurav", "Agarwal"} not in rem_names
    assert len(book) == 3
