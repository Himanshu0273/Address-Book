import pytest
from address_book_main import AddressBook
from address_book_system import AddressBookMain

@pytest.fixture
def contact_1():
    return {
        "first_name": "Himanshu",
        "last_name": "Baid",
        "address": "Ideal Grand",
        "city": "Howrah",
        "state": "West Bengal",
        "zip": "711102",
        "phone_number": "8910322481",
        "email": "himanshu@example.com"
    }

@pytest.fixture
def contact_2():
    return {
        "first_name": "Kamal",
        "last_name": "Baid",
        "address": "Ideal Grand",
        "city": "Howrah",
        "state": "West Bengal",
        "zip": "711102",
        "phone_number": "9830144378",
        "email": "kamal@example.com"
    }
 
@pytest.fixture   
def contact_3():
    return {
        "first_name": "Himanshu",
        "last_name": "Agarwal",
        "address": "Airport",
        "city": "Kolkata",
        "state": "West Bengal",
        "zip": "700029",
        "phone_number": "9876504321",
        "email": "gaurav@example.com"
    }

@pytest.fixture
def contact_4():
    return {
        "first_name": "Krish",
        "last_name": "Jain",
        "address": "Abode Valley",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "zip": "703203",
        "phone_number": "9807654321",
        "email": "krish@example.com"
    }
    
@pytest.fixture
def contact_5():
    return{
        "first_name": "Chirag",
        "last_name": "Baid",
        "address": "Vivek Vihar",
        "city": "Howrah",
        "state": "West Bengal",
        "zip": "711102",
        "phone_number": "9807657432",
        "email": "cb@gmail.com"
    }
    
@pytest.fixture
def address_book_with_five_contacts(contact_1, contact_2, contact_3, contact_4, contact_5):
    book = AddressBook()
    book.add_contact(**contact_1)
    book.add_contact(**contact_2)
    book.add_contact(**contact_3)
    book.add_contact(**contact_4)
    book.add_contact(**contact_5)
    return book


@pytest.fixture
def multiple_books(contact_1, contact_2, contact_3, contact_4, contact_5):
    manager = AddressBookMain()
    
    #Book1
    manager.add_book("Friends")
    manager.get_book("Friends").add_contact(**contact_3)
    manager.get_book("Friends").add_contact(**contact_4)
    manager.get_book("Friends").add_contact(**contact_5)
    
    #Book2
    manager.add_book("Family")
    manager.get_book("Family").add_contact(**contact_1)
    manager.get_book("Family").add_contact(**contact_2)
    
    return manager

