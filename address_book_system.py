from address_book_main import AddressBook
from Schema.schema import ContactSchema,contact_details
class AddressBookMain:
    
    def __init__(self):
        self.books = {}
    # Add a new Address Book
    def add_book(self):
        name = input("Enter the name of the address book: ")
        if name not in self.books:
            self.books[name] = AddressBook()
            print(self.books[name])
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
    
    #Search people by the city or state across multiple address books
    # def search_people_by_location(self):
    #     area = input("Enter the state or area: ")
    #     for c in self.books:
    #         searched_res = AddressBook.search_city_or_state(area) 
    #         AddressBook.same_area.append(searched_res)
        
    # def count_of_people_in_same_location(self):
    #     print(len(AddressBook.same_area))

    # def list_of_same_area_people(self):
    #     print(AddressBook.same_area)
    
    # Display the names of the address books
    def display_books(self):
        if len(self.books) == 0:
            print("There are no address books right now!!")
        else:
            for i, name in enumerate(self.books, 1):
                print(f"{i}. {name}")



#Search Functions class

class SearchFunction(AddressBookMain):
    
    def __init__(self, books):
        super().__init__()
        self.books = books
        self.same_area=[]
        
    def search_by_city_or_state(self, area):
        area = area.lower()
        for book in self.books.values():
            for contact in book.details:
                if area in contact.city.lower() or area in contact.state.lower():
                    self.same_area.append(contact)
                    
        return self.same_area
    
    def count_people_in_same_area(self, res, area):
        print(f"Number of people in the {area} area is: {len(res)}")
        
    def list_people_in_same_location(self, res, area):
        if not res:
            print(f"No contacts found in the area: {area}")
        else:
            print(f"People in {area} are:")
            for contact in res:
                print(contact)
                print()
    