# Library Management System

## 1. Project Title

**Library Management System**

## 2. Project Overview

The Library Management System is a simple Python-based console application developed to manage basic library activities.

The system allows the user to maintain book and member records, issue books, return books, and view a basic library report.

The project uses Python concepts such as lists, dictionaries, functions, loops, conditional statements, and menu-driven programming.

The main aim of the project is to provide a simple and easy-to-use system for handling common library operations.

## 3. Features

### Book Management

* Add a new book
* View all books
* Store book ID, title, and author
* Display book availability

### Member Management

* Add a library member
* View registered members
* Store member ID and name

### Issue Book

* Issue an available book
* Store the book ID and member ID
* Change the book status to "Issued"

### Return Book

* Return an issued book
* Change the book status back to "Available"
* Remove the issue record

### Library Report

The system displays:

* Total number of books
* Number of available books
* Number of issued books
* Total number of members

## 4. Technologies Used

* **Programming Language:** Python
* **Interface:** Console / Command Line
* **Data Storage:** Python lists and dictionaries
* **Development Tools:** VS Code / IDLE / PyCharm
* **Version Control:** Git and GitHub

## 5. Project Structure

The current simplified version contains the main program in a single Python file:

```text
Library-Management-System/
│
├── library_management.py
├── README.md
└── statement.md
```

The Python file contains the complete implementation of the system.

## 6. Main Functional Modules

Although the project is implemented in one Python file, it contains separate functions for its major operations.

### 1. Book Management

The `add_book()` and `view_books()` functions manage book records.

### 2. Member Management

The `add_member()` and `view_members()` functions manage member records.

### 3. Issue and Return Management

The `issue_book()` and `return_book()` functions handle book issue and return operations.

### 4. Reporting

The `report()` function displays the current library statistics.

## 7. Installation and Setup

### Step 1: Install Python

Install Python 3.x on the computer.

Check whether Python is installed:

```bash
python --version
```
Open the project folder.

### Step 2: Run the Program

Run the following command:

```bash
python library_management.py
```

## 8. How to Use

After running the program, the main menu is displayed:

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View Books
3. Add Member
4. View Members
5. Issue Book
6. Return Book
7. Library Report
8. Exit
```

The user enters the number corresponding to the required operation.

### Example

To add a book:

```text
Enter your choice: 1
Enter Book ID: 101
Enter Book Title: Python Basics
Enter Author: John Smith

Book added successfully.
```

To view the books:

```text
Enter your choice: 2

--- Books ---
101 | Python Basics | John Smith | Available
```

## 9. Testing

The program can be tested using the following test cases:

| Test Case                 | Expected Result                           |
| ------------------------- | ----------------------------------------- |
| Add a book                | Book is added                             |
| View books                | Book details are displayed                |
| Add a member              | Member is added                           |
| View members              | Member details are displayed              |
| Issue available book      | Book status changes to Issued             |
| Issue already issued book | Message shows that book is already issued |
| Return issued book        | Book status changes to Available          |
| Return available book     | Message shows that book is not issued     |
| View library report       | Library statistics are displayed          |
| Invalid menu option       | Invalid choice message is displayed       |

## 10. Input and Output

### Input

The system accepts:

* Book ID
* Book title
* Author name
* Member ID
* Member name
* Menu choice

### Output

The system displays:

* Book records
* Member records
* Issue and return messages
* Book availability
* Library statistics
* Error messages for invalid operations

## 11. Limitations

The current version has some limitations:

* Data is stored only while the program is running.
* There is no permanent database.
* There is no login system.
* There is no graphical user interface.
* There is no automatic fine calculation.
* The program is currently implemented in a single Python file.

## 12. Future Enhancements

The project can be improved by adding:

* Permanent file or database storage
* Admin login
* Student/member login
* Book search functionality
* Due dates
* Automatic fine calculation
* Book categories
* Graphical user interface
* SQLite or MySQL database
* Separate Python modules
* Automated testing

## 13. Conclusion

The Library Management System demonstrates how Python can be used to solve a simple real-world problem.

The project implements basic library operations through a menu-driven interface and uses functions, lists, dictionaries, loops, and conditional statements.

It provides a foundation that can be expanded into a more advanced library management application.
