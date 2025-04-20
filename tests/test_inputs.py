import pytest
from address_book_main import AddressBook
from address_book_system import AddressBookMain
from collections import Counter
def test_add_contacts(address_book_with_five_contacts):
    book = address_book_with_five_contacts

    assert len(book.details) == 5

    names = {(c.first_name, c.last_name) for c in book.details}
    expected_names = {
        ("Himanshu", "Baid"),
        ("Kamal", "Baid"),
        ("Gaurav", "Agarwal"),
        ("Krish", "Jain"),
        ("Chirag", "Baid")
    }

    assert names == expected_names

#Test edit contact function
# def test_edit_details(address_book_with_four_contacts):
#     pass

#Test the delete contact functionality
def test_delete_contact(address_book_with_five_contacts):
    book = address_book_with_five_contacts
    assert len(book)==5
    
    book.delete_details("Gaurav", "Agarwal")
    rem_names = {(c.first_name, c.last_name) for c in book.details}
    assert {"Gaurav", "Agarwal"} not in rem_names
    assert len(book) == 4
    
    
    
#Test for multiple address books:
def test_multiple_address_books(multiple_books):
    manager = multiple_books
    
    assert "Friends" in manager.books
    assert "Family" in manager.books
    
    friends = manager.get_book("Friends")
    family = manager.get_book("Family")
    
    assert len(friends)==3
    assert len(family)==2
    
    friends_names = [' '.join([c.first_name,c.last_name]) for c in friends.details]
    family_names = [' '.join([c.first_name,c.last_name]) for c in family.details]
    
    assert "Himanshu Baid" in family_names
    assert "Kamal Baid" in family_names
    assert "Chirag Baid" in friends_names
    assert "Gaurav Agarwal" in friends_names
    assert "Krish Jain" in friends_names
    assert "Aniket Sonar" not in friends_names

#no duplicates
def test_no_duplicates(multiple_books):
    manager = multiple_books
    
    #Duplicate Entries, should be denied
    assert manager.add_book("Friends") is False
    assert manager.add_book("Family") is False
    
    #Unique Name, should get added
    assert manager.add_book("Apartment") is True
    

