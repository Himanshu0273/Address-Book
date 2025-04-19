# from address_book_main import AddressBook
from address_book_system import AddressBookMain, SearchFunction
# from search_functions import SearchFunctions
class AddressBookManager:
    
    @staticmethod
    def display():
        print("Welcome to the Addresss Book!!!")
        
    def menu(self):
        address_book_library = AddressBookMain()
        searchfuncs = SearchFunction(address_book_library.books)
        while True:
            print("""
        Menu:
        
        1.Enter 1 to add a new Address Book to the Library.
        2.Enter 2 to get a book's details.
        3.Enter 3 to operate on a book.
        4.Enter 4 to find people in the same city or state across all the different address books.
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

            #UC8,9,10
            if book_choice == 4:
                area= input("Enter the city or state you want to search: ").lower()
                res = searchfuncs.search_by_city_or_state(area)
                searchfuncs.count_people_in_same_area(res,area)
                searchfuncs.list_people_in_same_location(res,area)
                    
            if book_choice == 9:
                address_book_library.display_books()
                
            if book_choice == 0:
                print("END")
                break

AddressBookManager.display()
mainobj = AddressBookManager()
mainobj.menu()