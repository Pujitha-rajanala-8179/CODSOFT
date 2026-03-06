import os

FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME):
            for line in file:
                name,phone,email,address = line.strip().split(",")
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                })
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']}\n")

def add_contact(contacts):
    name = input("Enter name:")  
    phone =input("Enter phone number:")
    email =input("Enter Email:")
    address =input("Enter Address:")

    contacts.append({
        "name":name,
        "phone":phone,
        "email":email,
        "address":address,
    })
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for contact in contacts:
        print(f"Name: {contact['name']},phone: {contact['phone']}")

def search_contact(contacts):
    search = input("Enter name or phone to search:")
    found = False
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("contact not found.")

def update_contact(contacts):
    name = input("Enter the name of contact to update:")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new phone:")
            contact['email'] = input("Enter new email:")
            contact['address'] = input("Enter,new address:")
            save_contacts(contacts)
            print("Contact Updated Successfully!")
            return
        print("contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of contact to delete:")
    for contact in contacts:
        if contact['name'].lower() ==name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact Deleted Successfully!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5.Delete Contact")
        print("6.Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting programm. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

main()