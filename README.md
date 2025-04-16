UC2 - Add Contact to Address Book

Overview
This module enables the user to add a new contact to the address book via console input. It follows Object-Oriented Programming (OOP) principles and includes automated testing using pytest with fake data generation using the Faker library.

Features
Accepts user input via console to add a new contact.

Implements Object-Oriented Concepts:

Contact: encapsulates contact information.

AddressBookMain: manages the collection of contacts.

Validates and adds contact data to the address book.

Supports unit testing using pytest.

Uses the Faker library to generate realistic fake data for testing.

Architecture
Class	                    Responsibility
Contact	                    Stores personal contact details
AddressBookMain	            Collects input and manages the address book list
generate_faker_input.py	    Generates and writes fake contact data to a test file
test_address_book.py	    Pytest file for testing Contact creation and storage

Testing with pytest and Faker
Faker is used to generate multiple realistic fake contact entries.

These entries are stored in test_input.txt.

pytest reads the entries, converts them into Contact objects, and checks if they are added correctly to the address book.