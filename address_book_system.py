from address_book_main import AddressBook
from Schema.schema import ContactSchema,contact_details
from Text_File_IO.file_IO_txt import  save_book_to_txt, load_all_books
class AddressBookMain:
    
    def __init__(self):
        #Load from file
        self.books = load_all_books()
        
    # Add a new Address Book
    def add_book(self, name = None):
        if name is None:
            name = input("Enter the name of the address book: ")
        
        if name not in self.books:
            self.books[name] = AddressBook()
            save_book_to_txt(name, self.books[name])
            print(self.books[name])
            return True
        else:
            print("An address book with the same name already exists!!!")
            return False
            
    # Get an existing Address Book
    def get_book(self, book=None):
        if book is None:
            book = input("Enter the book you want to access: ")
        
        if book not in self.books:
            print("No such book found!!")
            return
        print(f"Found book: {book}")
        print(type(self.books.get(book)))
        return book
    
    # Do operations on the selected address book
    def operate_book(self):
        book_name = self.get_book()
        if book_name is None:
            print("The book does not exist!!!")
            return
        book = self.books[book_name]
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
                    print(f"Give your Details: to add to {book_name} book: ")
                    try:
                        contact_data = contact_details()
                        book.add_contact(**contact_data.__dict__)
                        
                        save_book_to_txt(book_name, book)
                        
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
                        
                        save_book_to_txt(book_name, book)

                # Delete an existing contact
                case 3:
                    print("Enter the name of the contact to delete: ")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    book.delete_details(first_name, last_name)
                    
                    save_book_to_txt(book_name, book)

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
    
    
    #Sort the people in address book by name
    def sort_by_name(self, book=None):
        if book is None:
            print("NO BOOK SEARCHED!!")
            return []
        
        address_book = self.get_book(book)
        if not address_book:
            print(f"No address book of the name: {book} was found!")
            return []
        
        sorted_book = sorted(address_book, key=lambda x: (x.first_name, x.last_name))
        return sorted_book
 
    #Sort by state
    def sort_by_state(self, book=None):
        if book is None:
            print("NO BOOK SEARCHED!!")
            return []
        
        address_book = self.get_book(book)
        if not address_book:
            print(f"No book of the name {book} was found!")
            return []
        
        sorted_book = sorted(address_book.details, key=lambda x: x.state.lower())
        return sorted_book
    
    #Sort by city
    def sort_by_city(self, book=None):
        if book is None:
            print("NO BOOK SEARCHED!!")
            return []
        
        address_book = self.get_book(book)
        if not address_book:
            print(f"No book of the name {book} was found!")
            return []
        
        sorted_book = sorted(address_book.details, key=lambda x: x.city.lower())
        return sorted_book

    #Sort by zip
    def sort_by_zip(self, book=None):
        if book is None:
            print("NO BOOK SEARCHED!!")
            return []
        
        address_book = self.get_book(book)
        if not address_book:
            print(f"No book of the name {book} was found!")
            return []
        
        sorted_book = sorted(address_book.details, key=lambda x: x.zip.lower())
        return sorted_book
        
        
        
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
        self.same_city=[]
        self.same_state=[]
        
    #Search 
    def search_by_city_or_state(self, area):
        area = area.lower()
        for book in self.books.values():
            for contact in book.details:
                if area in contact.city.lower() or area in contact.state.lower():
                    self.same_area.append(contact)
                       
        return self.same_area
    
    def people_in_same_city(self, city):
        self.same_city=[]
        for book in self.books.values():
            for contact in book.details:
                if city in contact.city.lower():
                    self.same_city.append(contact)
                    
        return self.same_city
    
    def people_in_same_state(self, state):
        self.same_state=[]
        for book in self.books.values():
            for contact in book.details:
                if state in contact.state.lower():
                    self.same_state.append(contact)
                    
        return self.same_state
    
    
    def count_people_in_same_area(self, res, area):
        print(f"Number of people in the {area} area is: {len(res)}")
        print()
        
    def list_people_in_same_location(self, res, area):
        if not res:
            print(f"No contacts found in the area: {area}")
        else:
            print(f"People in {area} are:")
            for contact in res:
                print(contact)
                print()
    