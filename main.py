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
        5.Enter 5 to find all people in same city or state in separate lists
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

            if book_choice == 4:
                area= input("Enter the city or state you want to search: ").lower()
                res = searchfuncs.search_by_city_or_state(area)
                searchfuncs.count_people_in_same_area(res,area)
                searchfuncs.list_people_in_same_location(res,area)
                
            if book_choice==5:
                choice=input("Great!! Now pick 'c' or 's' to get all contacts from a city or state respectively: ")
                if choice.lower() == 's':
                    state = input("Enter the state you want to check: ")
                    print(f"People is {state} state are: ")
                    print(searchfuncs.people_in_same_state(state))
                    
                elif choice.lower() == 'c':
                    city = input("Enter the city you want to check: ")
                    print(f"People is {city} city are: ")
                    print(searchfuncs.people_in_same_city(city))
                else:
                    print("Invalid Input!!Try again!!")
                    
            if book_choice == 9:
                address_book_library.display_books()
                
            if book_choice == 0:
                print("END")
                break

AddressBookManager.display()
mainobj = AddressBookManager()
mainobj.menu()