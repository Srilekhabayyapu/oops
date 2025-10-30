contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added successfully!")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def display_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts available.")

# Example usage
add_contact("Alice", "9876543210")
add_contact("Bob", "9123456780")
search_contact("Alice")
display_contacts()
