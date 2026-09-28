# Library Management System

## 1. Problem Statement

Managing books and members manually can make basic library operations difficult and time-consuming.

A library needs to keep track of available books, issued books, members, and book returns. Without a simple computerized system, it can be difficult to maintain and view these records efficiently.

The proposed Library Management System is a Python-based console application designed to handle basic library operations.

The system provides options to add and view books, add and view members, issue and return books, and generate a basic library report.

## 2. Project Objectives

The main objectives of the project are:

1. To develop a simple Library Management System using Python.
2. To maintain basic book records.
3. To maintain basic member records.
4. To manage book issue and return operations.
5. To display the availability status of books.
6. To generate a basic library report.
7. To apply Python programming concepts to a practical problem.
8. To create a simple menu-driven application.

## 3. Scope of the Project

The project focuses on the basic operations required in a small library.

The system includes:

* Adding books
* Viewing books
* Adding members
* Viewing members
* Issuing books
* Returning books
* Tracking book availability
* Viewing library statistics

The current project is limited to a console-based application and does not include advanced database, authentication, or graphical interface features.

## 4. Target Users

The intended users of the system are:

### Library Staff

Library staff can use the system to maintain basic book and member information and manage issue and return operations.

### Small Libraries

The system can be used as a basic computerized solution for small-scale library record management.

### Students

The project can also be used as a learning project for students to understand how Python programming concepts can be applied to a real-world problem.

## 5. High-Level Features

### Book Management

Users can add and view books.

Each book contains:

* Book ID
* Book title
* Author
* Availability status

### Member Management

Users can add and view library members.

Each member contains:

* Member ID
* Member name

### Book Issue

The system allows an available book to be issued to a member.

When a book is issued, its status changes from:

```text
Available → Issued
```

### Book Return

The system allows an issued book to be returned.

After returning the book, its status changes from:

```text
Issued → Available
```

### Library Report

The report function displays:

* Total books
* Available books
* Issued books
* Total members

## 6. Functional Requirements

### FR1 — Add Book

The system shall allow the user to enter and store book details.

### FR2 — View Books

The system shall display all books and their availability status.

### FR3 — Add Member

The system shall allow the user to add member details.

### FR4 — View Members

The system shall display registered members.

### FR5 — Issue Book

The system shall allow an available book to be issued.

### FR6 — Return Book

The system shall allow an issued book to be returned.

### FR7 — Generate Report

The system shall display basic library statistics.

## 7. Non-Functional Requirements

Based on the project guideline, the project should consider qualities such as usability, reliability, maintainability, and error handling.

### Usability

The system uses a simple menu-driven interface so that users can select operations easily.

### Reliability

The system checks whether a book exists and whether it is already issued before performing issue and return operations.

### Maintainability

The program uses separate functions for different operations, making the code easier to understand and modify.

### Error Handling

The program displays messages for invalid menu choices and invalid book operations.

## 8. Technology and Implementation

The project is developed using:

* Python
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Console input/output

The current implementation stores data in Python lists and dictionaries during program execution.

## 9. Basic Workflow

```text
Start
  |
  v
Main Menu
  |
  +---- Add/View Books
  |
  +---- Add/View Members
  |
  +---- Issue Book
  |
  +---- Return Book
  |
  +---- View Report
  |
  +---- Exit
  |
  v
End
```

## 10. Expected Outcome

The expected outcome is a working console-based Library Management System that can perform the basic operations defined in the project scope.

The system should allow users to manage book and member information, issue and return books, and view basic library statistics.

## 11. Limitations

The current version has the following limitations:

* Records are not permanently stored after the program closes.
* No login or authentication system is provided.
* No database is used.
* No graphical interface is provided.
* No fine calculation is included.
* The current version uses one Python source file.

## 12. Future Enhancements

Possible future improvements include:

* Database integration
* Login and authentication
* Fine calculation
* Due-date management
* Search and filtering
* GUI using Tkinter
* SQLite/MySQL integration
* Separate Python modules
* Automated testing
* Report export

## 13. Conclusion

The Library Management System is a simple Python project that demonstrates the practical use of programming concepts in a real-world library scenario.

The project provides basic book management, member management, book issue and return operations, and library reporting.

The current version provides a foundation that can be extended with permanent storage, authentication, databases, graphical interfaces, and additional library features.
