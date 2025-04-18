# from address_book_main import AddressBookMain
from address_book_system import AddressBookSystem
class AddressBookManager:
    
    @staticmethod
    def display():
        print("Welcome to the Addresss Book!!!")
        
    def menu(self):
        address_book_library = AddressBookSystem()
        while True:
            print("""
        Menu:
        
        1.Enter 1 to add a new Address Book to the Library.
        2.Enter 2 to get a book's details
        3.Enter 3 to operate on a book                  
        9.Enter 9 to display the list of all available address books.
        0.Enter 0 to END.
                  """)
            book_choice = int(input("Enter your choice: "))
            if book_choice == 1:
                address_book_library.add_book()
            
            if book_choice == 2:
                address_book_library.get_book()
                
            if book_choice == 3:
                address_book_library.operate_book()

            if book_choice == 9:
                address_book_library.display_books()
                
            if book_choice == 0:
                print("END")
                break

AddressBookManager.display()
mainobj = AddressBookManager()
mainobj.menu()