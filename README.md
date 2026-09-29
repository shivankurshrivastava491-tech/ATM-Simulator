# ATM-Simulator
1. Project Title :- ATM Simulation System
A Python-based console application that simulates the basic operations of an Automated Teller Machine (ATM), including secure PIN login, balance checking, deposits, withdrawals, transaction history, account information, and PIN management.

2. Overview of the Project
The ATM Simulation System is a beginner-friendly Python project designed to demonstrate how a real-world ATM system can be represented using programming concepts.
The project provides a menu-driven interface through which a user can log in using a PIN and perform different banking operations. Account information and transaction records are stored in a JSON file, allowing the data to remain available even after the program is closed.
The project focuses on applying Python concepts such as functions, conditional statements, loops, exception handling, file handling, JSON data management, and date/time handling.This project is implemented as a console-based Python application.

3.Features:-
Secure PIN Login
User authentication through a 4-digit PIN.
Maximum of 3 incorrect PIN attempts.
Account is automatically locked after 3 failed attempts.
Locked accounts cannot access the ATM menu.
Balance Management:-
Check the current account balance.
Deposit money into the account.
Withdraw money from the account.
Prevents withdrawal when the requested amount is greater than the available balance.
Rejects invalid or non-positive transaction amounts.
Transaction History:
Records deposits and withdrawals.
Stores the transaction type, amount, and date/time.
Displays all recorded transactions.
Account Information:-
Displays:
Account holder name
Account number
Phone number
Email address
Change PIN
Allows the user to change the existing PIN.
Verifies the current PIN first.
Requires a new PIN to contain exactly 4 digits.
Requires PIN confirmation.
Prevents using the same PIN as the old PIN.
Data Persistence
Account information is stored in atm_data.json.
Changes to balance, PIN, lock status, and transactions are saved automatically.
Data is loaded when the application starts.
Menu-Driven Interface
The main ATM menu provides:
Check Balance
Deposit Money
Withdraw Money
Transaction History
Account Information
Change PIN
Exit

5.Technologies / Tools Used:-
Technology / Tool
Purpose
Python 3
Main programming language
JSON
Storing account and transaction data
Python json module
Reading and writing JSON data
Python os module
Checking whether the data file exists
Python datetime module
Recording transaction date and time
IDLE / VS Code 
Running and testing the program
Git & GitHub
Version control and project submission
Python Concepts Used
Variables and data types
Dictionaries and lists
Functions
if-elif-else conditions
while loops
try-except exception handling
File handling
JSON serialization/deserialization
User input
Date and time handling
Modular program structure

5. Project Structure:- 
ATM-Simulation/
atmsimulation-1.py
atm_data.json
README.md

File Description:- 
atmsimulation-1.py
Contains the complete Python source code.
Handles login, ATM menu, banking operations, PIN management, and transactions.
atm_data.json
Stores account information.
Stores current balance.
Stores PIN and account lock status.
Stores transaction history.
README.md
Contains project documentation, installation instructions, features, and testing instructions.

5. Project Structure
ATMSimulation/
atmsimulation-1.py
atm_data.json
README.md
File Description
atmsimulation-1.py
Contains the complete Python source code.
Handles login, ATM menu, banking operations, PIN management, and transactions.
atm_data.json
Stores account information.
Stores current balance.
Stores PIN and account lock status.

Stores transaction history.
README.md
Contains project documentation, installation instructions, features, and testing instructions.

7. Installation & Setup
Step 1: Install Python
Install Python 3 on your computer.
Check whether Python is installed:
python --version

Step 2: Download / Clone the Repository
Clone the GitHub repository:git clone <YOUR-GITHUB-REPOSITORY-URL>
Move into the project folder:
cd ATM-Simulation
Alternatively, download the repository as a ZIP file and extract it.

Step 3: Check the Project Files
Make sure the following files are in the same folder:
atmsimulation-1.py
atm_data.json
README.md
Step 4: Run the Program
Using the terminal:
python atmsimulation-1.py
You can also open atmsimulation-1.py in IDLE and select:
Run → Run Module

7. How to Use the Project
Step 1: Start the Application
After running the program, the following type of welcome screen is displayed
Step 2: Enter the PIN
Enter the account PIN when prompted.
The program checks the entered PIN against the account information stored in atm_data.json.
For security, do not publish real account details or PINs in a public GitHub repository. For testing, use the PIN configured in your local atm_data.json file.
Step 3: Select an ATM Operation
After successful login, the ATM menu is displayed:

  ATM MENU
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Account Information
6. Change PIN
7. Exit
Enter the number corresponding to the operation you want to perform.

8. Instructions for Testing
The following test cases can be used to verify the main functionality of the project.

<img width="330" height="182" alt="image" src="https://github.com/user-attachments/assets/9a6c43ec-db85-47c6-bc94-fbccb96c38a1" /><img width="318" height="267" alt="image" src="https://github.com/user-attachments/assets/f1408010-715c-496d-a4cf-650a9b7c7a3d" /><img width="301" height="316" alt="image" src="https://github.com/user-attachments/assets/ba62c33d-cf8d-4891-9058-795054e026db" /><img width="317" height="362" alt="image" src="https://github.com/user-attachments/assets/0c477071-8c15-4b24-9856-442e8b454074" /><img width="306" height="352" alt="image" src="https://github.com/user-attachments/assets/927373c5-ee1d-4e96-98e6-4d85bb9f4122" /><img width="403" height="393" alt="image" src="https://github.com/user-attachments/assets/0c3954aa-fbae-4bfa-88c6-58a98df1e7ef" /><img width="391" height="406" alt="image" src="https://github.com/user-attachments/assets/5acdcb44-38da-40b8-8a48-5f103090b480" /><img width="333" height="412" alt="image" src="https://github.com/user-attachments/assets/acba1bf9-9171-46d5-8610-ed4c46991103" /><img width="317" height="327" alt="image" src="https://github.com/user-attachments/assets/bcb422a3-81a5-4a32-b530-0172270fccdb" />

11. Program Workflow  
Start
Load account data from JSON
Check account lock status
Locked  Display locked message
End  
Enter PIN
Incorrect
Count attempt
attempts Lock account
End 
Login Successful
Display ATM Menu
Check Balance
Deposit Money
Withdraw Money
Transaction History
Account Information
Change PIN
Exit
End
