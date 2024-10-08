# Initialize an empty dictionary to store contacts
contacts = {}

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def list_contacts():
    if contacts:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter the contact name: ")
            phone = input("Enter the phone number (10 digits): ")
            if is_valid_phone(phone):
                add_contact(name, phone)
            else:
                print("Invalid phone number. Please enter 10 digits only.")

        elif choice == '2':
            name = input("Enter the contact name to delete: ")
            delete_contact(name)

        elif choice == '3':
            list_contacts()

        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
