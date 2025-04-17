case 2:
                    print("Enter the name to edit details: ")
                    if len(address_book.details)==0:
                        print("ADDRESS BOOK IS EMPTY")
                    else:
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        address_book.edit_details(first_name, last_name)
                