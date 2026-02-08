# Contact Book Application
# Stores contacts as: {name: {"phone": "123", "email": "abc@xyz"}}
# Saves to "contacts.txt" so data persists after you close the program.

import json
import os

# File where we save and load contacts.
# We use JSON format: the dictionary is converted to text (e.g. {"Alice": {"phone": "111", "email": "a@b.com"}})
# so it can be written to a file, and we convert it back to a dict when we load.
CONTACTS_FILE = "contacts.txt"


def load_contacts():
    """
    Load contacts from the file when the program starts.
    - If the file doesn't exist yet (first run), we return an empty dictionary.
    - We read the file as text, then use json.load() to turn that text back into a Python dict.
    """
    if not os.path.exists(CONTACTS_FILE):
        return {}
    try:
        with open(CONTACTS_FILE, "r") as f:
            contacts = json.load(f)
        return contacts
    except (json.JSONDecodeError, IOError):
        return {}


def save_contacts(contacts):
    """
    Save the contacts dictionary to the file.
    - json.dumps() converts our dict into a string (e.g. '{"Alice": {"phone": "111", "email": "a@b.com"}}').
    - We write that string to the file so we can read it back later with json.load().
    """
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts):
    """Ask for name, phone, email and add them to the contacts dict."""
    try:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if name in contacts:
            print("A contact with that name already exists.")
            return
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact added successfully.")
    except Exception as e:
        print(f"Error adding contact: {e}")


def view_contacts(contacts):
    """Show all contacts. Each contact is stored as name -> {phone, email}."""
    if not contacts:
        print("No contacts yet.")
        return
    print("\n--- All contacts ---")
    for name, info in contacts.items():
        print(f"  {name}: phone={info['phone']}, email={info['email']}")
    print()


def search_contact(contacts):
    """Search by name (case-insensitive)."""
    search_name = input("Enter name to search: ").strip()
    if not search_name:
        print("Please enter a name.")
        return
    search_lower = search_name.lower()
    found = False
    for name, info in contacts.items():
        if name.lower() == search_lower:
            print(f"Found: {name} - phone={info['phone']}, email={info['email']}")
            found = True
            break
    if not found:
        print("No contact found with that name.")


def delete_contact(contacts):
    """Remove a contact by name."""
    name = input("Enter name to delete: ").strip()
    if not name:
        print("Please enter a name.")
        return
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("No contact found with that name.")


def main():
    # Load contacts from file when program starts (empty dict if file doesn't exist).
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
