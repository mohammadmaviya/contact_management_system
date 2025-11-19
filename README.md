# contact_management_system
📒 Contact Management System (Python)
A simple command-line Contact Book Application written in Python.
This project allows users to create, view, update, search, count, and delete contacts using a dictionary-based data structure.

🚀 Features
•	➕ Create Contact – Add a new contact with name, age, email, and mobile number
•	📄 View All Contacts – Display all saved contacts
•	✏️ Update Contact – Modify existing contact details
•	🔍 Search Contact – Search for a contact by name (case-insensitive)
•	🔢 Count Contacts – Shows the total number of saved contacts
•	🗑️ Delete Contact – Remove a specific contact
•	🚪 Exit the application safely

🧠 How It Works
The app uses a Python dictionary:
contacts = {
    "John": {"age": 19, "email": "maviya@gmail.com", "mobile": 9876543210}
}
Each contact is stored as a key-value pair, where:
•	Key ➝ contact name
•	Value ➝ another dictionary holding age, email, mobile

🖥️ Program Flow
1.	User is shown a menu of options
2.	Input is taken through the terminal
3.	Based on the choice, CRUD operations are performed
4.	The loop continues until the user selects Exit (7)

