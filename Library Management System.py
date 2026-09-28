books = []
members = []
x = []
def add():
    id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    books.append({
        "id": id,
        "name": title,
        "author": author,
        "available": True
    })
    print("Book added successfully.")
def view():
    if not books:
        print("No books available.")
        return
    print("\n--- Books ---")
    for book in books:
        if book["available"]:
            status = "Available"
        else:
            status = "Issued"

        print(
            book["id"],
            "|", book["title"],
            "|", book["author"],
            "|", status
        )
def add_member():
    member_id = int(input("Enter Member ID: "))
    name = input("Enter Member Name: ")

    members.append({
        "id": member_id,
        "name": name
    })
    print("Member added successfully.")
def view_members():
    if not members:
        print("No members available.")
        return
    print("\n--- Members ---")
    for member in members:
        print(member["id"], "|", member["name"])
def issue_book():
    id = int(input("Enter Book ID: "))
    member_id = int(input("Enter Member ID: "))
    for book in books:
        if book["id"] == id:
            if not book["available"]:
                print("Book is already issued.")
                return
            book["available"] = False
            x.append({
                "id": id,
                "member_id": member_id
            })
            print("Book issued successfully.")
            return
    print("Book not found.")
def return_book():
    id = int(input("Enter Book ID: "))
    for book in books:
        if book["id"] == id:
            if book["available"]:
                print("Book is not issued.")
                return
            book["available"] = True
            for record in x:
                if record["id"] == id:
                 x.remove(record)
                 break
            print("Book returned successfully.")
            return
    print("Book not found.")
def report():
    available = 0
    issued = 0
    for book in books:f
        if book["available"]:
            available += 1
        else:
            issued += 1
    print("\n--- Library Report ---")
    print("Total Books     :", len(books))
    print("Available Books :", available)
    print("Issued Books    :", issued)
    print("Total Members   :", len(members))

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Library Report")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        add_member()
    elif choice == "4":
        view_members()
    elif choice == "5":
        issue_book()
    elif choice == "6":
        return_book()
    elif choice == "7":
        report()
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
