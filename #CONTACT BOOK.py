#CONTACT BOOK

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully!")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self):
        name = input("Enter name of contact to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            self.contacts[name] = {"phone": phone, "email": email}
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self):
        name = input("Enter name of contact to search: ")
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        if self.contacts:
            print("\nContact Book:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}\n")
        else:
            print("Contact book is empty.")

    def run(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Update Contact")
            print("4. Search Contact")
            print("5. Display Contacts")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.delete_contact()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.search_contact()
            elif choice == "5":
                self.display_contacts()
            elif choice == "6":
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
