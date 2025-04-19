import pytest
from address_book_main import AddressBook

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
        "first_name": "Gaurav",
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
        "zip": "603203",
        "phone_number": "9807654321",
        "email": "krish@example.com"
    }
    
@pytest.fixture
def address_book_with_four_contacts(contact_1,contact_2,contact_3,contact_4):
    book = AddressBook()
    book.add_contact(**contact_1)
    book.add_contact(**contact_2)
    book.add_contact(**contact_3)
    book.add_contact(**contact_4)
    return book
