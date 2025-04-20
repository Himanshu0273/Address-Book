import os
from address_book_main import AddressBook
from contact_info import Contact

DATA_DIR = "Text_File_IO/data/"


os.makedirs(DATA_DIR, exist_ok=True)


def save_book_to_txt(book_name, address_book: AddressBook):
    """ Save the AddressBook's contacts to a text file. """
    file_path = os.path.join(DATA_DIR, f"{book_name}.txt")
    
    with open(file_path, "w") as file:
        for contact in address_book.details:
            file.write(f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},{contact.state},{contact.zip},{contact.phone_number},{contact.email}\n")
    
    print(f"Address Book '{book_name}' saved to {file_path}")
    
    
def load_book_from_txt(book_name)->AddressBook:
    file_path = os.path.join(DATA_DIR, f"{book_name}.txt")
    address_book = AddressBook()
    
    if not os.path.exists(file_path):
        print("No file of the name {book_name} found!!!")
        return address_book
    
    
    with open(file_path, "r") as file:
        for line in file:
            first_name, last_name, address, city, state, zip_code, phone_number, email = line.strip.split(',')
            contact = Contact(first_name = first_name, last_name=last_name, address=address, city=city, state=state, zip=zip_code, phone_number=phone_number, email=email)
            address_book.details.append(contact)
            
        print(f"Address book '{book_name}' loaded from {file_path}")
        return address_book
    
    
def load_all_books() -> dict:
        """ Load all saved books into a dictionary. """
        books = {}
        for filename in os.listdir(DATA_DIR):
            if filename.endswith(".txt"):
                book_name = filename[:-4]
                books[book_name] = load_book_from_txt(book_name)
        return books