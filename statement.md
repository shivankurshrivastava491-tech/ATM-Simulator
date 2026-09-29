Project Title

ATM Simulation System

1. Problem Statement:-

Traditional ATM systems are complex software systems connected to banking networks and specialized hardware. For learning and academic purposes, it is useful to understand the basic working of an ATM through a simple software simulation.

The ATM Simulation System is developed as a Python-based console application that represents the core operations of an ATM in a simple and understandable way. The system allows a user to authenticate using a PIN and perform common banking operations such as checking the account balance, depositing money, withdrawing money, viewing transaction history, checking account information, and changing the PIN.

The project also addresses basic security and data-management requirements. It limits the number of incorrect PIN attempts and locks the account after three failed attempts. Account and transaction information are stored in a JSON file so that changes can be maintained between program executions.

The project is intended to demonstrate how Python programming concepts can be applied to a real-world problem in a structured and practical way.

2. Scope of the Project:-

The scope of the project is to develop a basic ATM simulation using Python without requiring a web application, external banking system, or ATM hardware.

The project covers:

User authentication using a PIN.

Limiting incorrect PIN attempts.

Locking the account after three failed login attempts.

Checking the current account balance.

Depositing money.

Withdrawing money.

Preventing withdrawals greater than the available balance.

Recording deposits and withdrawals.

Displaying transaction history.

Displaying basic account information.

Changing the account PIN.

Saving account and transaction information in a JSON file.

Loading previously saved information when the program starts.

Providing a simple menu-driven console interface.

Out of Scope

The current version does not provide:

Real banking transactions.

Connection to a bank server.

ATM hardware integration.

Multiple-bank/network connectivity.

Online or mobile banking.

Production-level encryption or authentication.

A graphical or web-based user interface.

These features can be considered for future versions of the project.

3. Target Users:-

The primary target users of this project are:

3.1 Students:-

Students can use the project to understand how programming concepts can be applied to a practical banking-related problem.

3.2 Beginner Python Programmers:-

The project is suitable for beginners who want to practice:

Functions

Loops

Conditional statements

Dictionaries and lists

File handling

JSON

Exception handling

User input

Date and time handling
3.3 Academic Evaluators:-

Teachers and evaluators can use the project to assess the implementation of programming concepts through a real-world simulation.

3.4 Users Learning ATM Workflow:-

The application can also be used as a simple demonstration of the basic workflow involved in an ATM transaction.

4. High-Level Features:-

4.1 PIN-Based Authentication

The system asks the user to enter a PIN before providing access to ATM operations.

The user gets a maximum of three login attempts. After three incorrect attempts, the account is locked.

4.2 Balance Checking:-

The user can view the current account balance through the ATM menu.

4.3 Deposit Money:-

The user can enter an amount to deposit. If the amount is valid and greater than zero, it is added to the account balance and recorded as a transaction.

4.4 Withdraw Money:-

The user can withdraw money from the account. The system checks whether the requested amount is valid and whether sufficient balance is available before completing the transaction.

4.5 Transaction History:-

The system records deposits and withdrawals with their transaction type, amount, and date/time. The user can view the stored transaction history.

4.6 Account Information:-

The system displays basic account information such as the account holder's name, account number, phone number, and email address.

4.7 Change PIN:-

The user can change the existing PIN after entering the current PIN. The system validates the new PIN and its confirmation before saving the change.

4.8 JSON-Based Data Storage:-

The project stores account information and transaction records in a JSON file. This allows changes made during one program execution to remain available when the program is run again.

4.9 Input Validation:-

The application checks for common invalid inputs, including:

Invalid menu choices

Invalid transaction amounts

Zero or negative amounts

Insufficient balance

Incorrect PIN

Invalid PIN format

Mismatched PIN confirmation

4.10 Menu-Driven Interface:-

The system provides a simple numbered menu so that users can select the required ATM operation from the console.

END 
