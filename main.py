from address_book_main import AddressBookMain
class AddressBook:
    
    @staticmethod
    def display():
        print("Welcome to the Addresss Book!!!")
        
    def menu(self):
        address_book = AddressBookMain()
        while True:
            print("""
                Menu:
                1. Enter 1 to add contact details.
                9. Enter 9 to display the address book.
                END: Enter 0 to stop.
                """)
            choice = int(input("Enter your choice: "))
            
            match choice:
                case 1:
                    print("Give your details to add to the address book: ")
                    first_name=input("First Name: ")
                    last_name=input("Last Name: ")
                    address=input("Address: ")
                    city=input("City: ")
                    state=input("State: ")
                    zip=input("ZIP Code: ")
                    phno=input("Phone Number: ")
                    email=input("Email ID: ")
                    try:
                        address_book.add_contact(
                            first_name=first_name,
                            last_name=last_name,
                            address=address,
                            city=city,
                            state=state,
                            zip=zip,
                            phno=phno,
                            email=email                            
                        )              
                    except ValueError as e:
                        print(e)
                    
                    
                # case 2:
                #     print("Enter the first name to edit details: ")
                case 9:
                    print("Here's your address book: ")
                    address_book.display_details()
                case 0:
                    print("END")
                    break
                case _:
                    print("Invalid input, try again.")


AddressBook.display()
mainobj = AddressBook()
mainobj.menu()