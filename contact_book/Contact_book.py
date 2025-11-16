def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")
    print(" Contact added")


def view_contacts():
    with open("contacts.txt","r") as f:
        data = f.readlines()

    print("\n---- CONTACT LIST ----")
    for line in data:
        name, phone = line.strip().split(",")
        print(f"name: {name} | Phone: {phone}")
        print("-----------------------")

def search_contact():
    search = input("Enter name to search: ").lower()
    found = False

    with open("contacts.txt","r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            if search in name.lower():
                print(f"Found -> {name} : {phone}")
                found = True

    if not found:
        print(" Contact not found")


def delete_contact():
    name_to_delete = input("Enter name to delete: ").lower()

    with open("contacts.txt", "r") as f:
        line = f.readlines()

    with open("contacts.txt","w") as f:
        for line in line:
            name , phone = line.strip().splite(",")
            if name.lower() != name_to_delete:
                f.write(line)
    
    print(" Delete successfully")

def menu():
        while True:
            print("""
====== CONTACT BOOK ======
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
""")
            choice = input("Enter choice: ")
            if choice == "1":
                add_contact()
            elif choice == "2":
                view_contacts()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                delete_contact()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print(" Invalid Option")

menu()