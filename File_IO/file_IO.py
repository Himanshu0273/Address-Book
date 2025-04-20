import os
import csv
import json
from address_book_main import AddressBook
from contact_info import Contact

DATA_DIR_TXT = "File_IO/data_txt/"
DATA_DIR_CSV = "File_IO/data_csv/"
DATA_DIR_JSON = "File_IO/data_json/"

os.makedirs(DATA_DIR_TXT, exist_ok=True)
os.makedirs(DATA_DIR_CSV, exist_ok=True)
os.makedirs(DATA_DIR_JSON, exist_ok=True)

# -----------------------TEXT FILES-----------------------

def save_book_to_txt(book_name, address_book: AddressBook):
    file_path = os.path.join(DATA_DIR_TXT, f"{book_name}.txt")
    
    with open(file_path, "w") as file:
        for contact in address_book.details:
            file.write(f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},{contact.state},{contact.zip},{contact.phone_number},{contact.email}\n")
    
    print(f"Address Book '{book_name}' saved to {file_path}")

def load_book_from_txt(book_name) -> AddressBook:
    file_path = os.path.join(DATA_DIR_TXT, f"{book_name}.txt")
    address_book = AddressBook()
    
    if not os.path.exists(file_path):
        print(f"No file of the name {book_name} found!!!")
        return address_book

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue 
            parts = line.split(',')
            if len(parts) != 8:
                print(f"Skipping malformed line in {book_name}.txt: {line}")
                continue
            first_name, last_name, address, city, state, zip_code, phone_number, email = parts
            contact = Contact(first_name=first_name, last_name=last_name, address=address, city=city, state=state, zip=zip_code, phone_number=phone_number, email=email)
            address_book.details.append(contact)

    print(f"Address book '{book_name}' loaded from {file_path}")
    return address_book

# -----------------------CSV FILES-----------------------

def save_book_to_csv(book_name, address_book: AddressBook):
    file_path = os.path.join(DATA_DIR_CSV, f"{book_name}.csv")
    
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Address', 'City', 'State', 'ZIP Code', 'Phone Number', 'Email'])
        
        for c in address_book.details:
            writer.writerow([c.first_name, c.last_name, c.address, c.city, c.state, c.zip, c.phone_number, c.email])
    
    print(f"Address book '{book_name}' saved to {file_path}")

def load_book_from_csv(book_name) -> AddressBook:
    file_path = os.path.join(DATA_DIR_CSV, f"{book_name}.csv")
    address_book = AddressBook()
    
    if not os.path.exists(file_path):
        print(f"No file of the name {book_name} found!!!")
        return address_book

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            first_name, last_name, address, city, state, zip_code, phone_number, email = row
            contact = Contact(first_name=first_name, last_name=last_name, address=address, city=city, state=state, zip=zip_code, phone_number=phone_number, email=email)
            address_book.details.append(contact)

    print(f"Address book '{book_name}' loaded from {file_path}")
    return address_book

# -----------------------JSON FILE-----------------------

def save_book_to_json(book_name, address_book: AddressBook):
    file_path = os.path.join(DATA_DIR_JSON, f"{book_name}.json")
    
    book_dict = {
        "contacts": [
            {
                "first_name": contact.first_name,
                "last_name": contact.last_name,
                "address": contact.address,
                "city": contact.city,
                "state": contact.state,
                "zip": contact.zip,
                "phone_number": contact.phone_number,
                "email": contact.email
            }
            for contact in address_book.details
        ]
    }
    
    with open(file_path, "w") as file:
        json.dump(book_dict, file, indent=4)
    
    print(f"Address Book '{book_name}' saved to file {file_path}")

def load_book_from_json(book_name) -> AddressBook:
    file_path = os.path.join(DATA_DIR_JSON, f"{book_name}.json")
    address_book = AddressBook()
    
    if not os.path.exists(file_path):
        print(f"No file of the name '{book_name}' found!!")
        return address_book
    
    with open(file_path, "r") as file:
        book_dict = json.load(file)
        for c in book_dict['contacts']:
            contact = Contact(
                first_name=c['first_name'],
                last_name=c['last_name'],
                address=c["address"],
                city=c["city"],
                state=c["state"],
                zip=c["zip"],
                phone_number=c["phone_number"],
                email=c["email"]
            )
            address_book.details.append(contact)

    print(f"Address book '{book_name}' loaded from {file_path}")
    return address_book

# -----------------------LOAD ALL BOOKS-----------------------

def load_all_books() -> dict:
    books = {}

    for filename in os.listdir(DATA_DIR_TXT):
        if filename.endswith(".txt"):
            book_name = filename[:-4]
            books[book_name] = load_book_from_txt(book_name)

    for filename in os.listdir(DATA_DIR_CSV):
        if filename.endswith(".csv"):
            book_name = filename[:-4]
            books[book_name] = load_book_from_csv(book_name)

    for filename in os.listdir(DATA_DIR_JSON):
        if filename.endswith(".json"):
            book_name = filename[:-5]
            books[book_name] = load_book_from_json(book_name)

    return books
