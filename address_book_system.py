from address_book_main import AddressBookMain
from Schema.schema import ContactSchema,contact_details
class AddressBookSystem:
    
    def __init__(self):
        self.books = {}
        
    # Add a new Address Book
    def add_book(self):
        name = input("Enter the name of the address book: ")
        if name not in self.books:
            self.books[name] = AddressBookMain()
        else:
            print("An address book with the same name already exists!!!")
            
    # Get an existing Address Book
    def get_book(self):
        book = input("Enter the book you want to access: ")
        if book is None:
            print("No such book found!!")
            return
        print(f"Found book: {book}")
        return self.books.get(book)
    
    # Do operations on the selected address book
    def operate_book(self):
        book = self.get_book()
        if book is None:
            print("The book does not exist!!!")
            return
        while True:
            print("""
    Menu:

    1. Enter 1 to add new contact details.
    2. Enter 2 to edit existing contact details.
    3. Enter 3 to delete an existing contact.
    9. Enter 9 to display the address book.
    END: Enter 0 to stop.
            """)
            choice = int(input("Enter your choice: "))

            match choice:
                # Add a contact
                case 1:
                    print(f"Give your Details: to add to {book} book: ")
                    try:
                        contact_data = contact_details()
                        book.add_contact(**contact_data.__dict__)
                    except ValueError as e:
                        print(f"Error: {e}")
                # Edit an existing contact
                case 2:
                    if len(book.details) == 0:
                        print("ADDRESS BOOK IS EMPTY")
                    else:
                        print("Enter the name to edit details: ")
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        book.edit_details(first_name, last_name)

                # Delete an existing contact
                case 3:
                    print("Enter the name of the contact to delete: ")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    book.delete_details(first_name, last_name)

                # Display contact details
                case 9:
                    print("Here's your address book: ")
                    book.display_details()

                # End
                case 0:
                    print("END")
                    return

                # Invalid input
                case _:
                    print("Invalid input, try again.")
    
    # Display the names of the address books
    def display_books(self):
        if len(self.books) == 0:
            print("There are no address books right now!!")
        else:
            for i, name in enumerate(self.books, 1):
                print(f"{i}. {name}")
