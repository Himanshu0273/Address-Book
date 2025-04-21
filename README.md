# 📒 Address Book Management System

A Python-based modular Address Book System that allows users to create and manage multiple address books, each containing validated contact information. The system supports full CRUD operations, advanced search capabilities, and persistent storage across `.txt`, `.csv`, and `.json` formats. Powered by `pydantic` for schema validation and a clean CLI interface.

---

## 🚀 Features

- 🔹 Create and manage multiple address books
- 🔹 Add, edit, delete, and display contacts
- 🔹 Validate contact details using `Pydantic`
- 🔹 Store data in `.txt`, `.csv`, and `.json` formats
- 🔹 Search people across all address books by:
  - City
  - State
- 🔹 Count and list contacts in a specific location
- 🔹 Sort contacts by:
  - Name
  - City, State, or ZIP
- 🔹 Interactive and user-friendly CLI menus

---

## 🗂️ Project Structure

AddressBookProject/  
├── Schema/  
│ ├── schema.py/
├── Utils/  
│ ├── validate_input.py
├──tests/  
│ └── test_inputs.py 
│ └── conftest.py
├── File_IO/  
│ ├── data_txt/ 
│ ├── data_csv/  
│ ├── data_json/
│ └── file_IO.py  
├── address_book_main.py  
├── main.py  
├── address_book.py  
├── address_book_system.py  
├── contact_info.py
├── README.md
├── requirements.txt



---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Pydantic** – for input validation
- **CSV / JSON / TXT** – for persistent file storage
- **CLI Interface** – no GUI required

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/address-book-system.git
cd address-book-system
```
### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```

### 🧑‍💻 How to Use
On running main.py, you'll be presented with a numbered menu. Select operations like:

Add new books

Open a book and perform contact operations

Find people across books by city/state

Sort contacts by different fields

View all books or exit

All changes are saved automatically to all 3 file formats.

### ✅ Sample Contact Fields
When adding a contact, you'll be asked to input:

First Name

Last Name

Address

City

State

ZIP Code

Phone Number

Email

All fields are validated using the Pydantic ContactSchema.

### 📁 Data Storage
For every address book created, the system generates:

File_IO/data_txt/<book_name>.txt

File_IO/data_csv/<book_name>.csv

File_IO/data_json/<book_name>.json

This ensures redundancy and multiple formats for portability.

### 📄 Requirements

```text
pydantic>=2.0
```
### 📬 Contact
## Made by Himanshu Baid
If you found this useful, feel free to ⭐️ the repo or connect with me on LinkedIn!

LinkedIn: https://www.linkedin.com/in/himanshu-baid-808834213/