# Capstone Project 1 - Employee Management System (EMS)
Employee Management System (EMS) is designed to manage &amp; evaluate employee records. The system allows users to Create, Read, Update, &amp; Delete (CRUD) employee data (personal information, job performance,&amp; attendance records). By integrating it, this program demonstrates a practical approach to basic HR analytics &amp; payroll logic using Python fundamentals. 

## Data Structure

Employee data is stored in a list of dictionaries, where each dictionary represents one employee with the following attributes:

- NIP         : Employee Identification Number
- Name        : Employee name
- Gender      : Gender
- Branch      : Work branch/location
- Performance : Performance grade (A, B, or C)
- Absence     : Number of absent days

## Program Features
### a. Main Menu

The program runs in a loop and provides a main menu with the following options:
- Employee Data Report
- Add Employee Data
- Edit Employee Data
- Delete Employee Data
- Employee Salary and Bonus
- Exit

### b. Employee Data Report (READ)

- All Employee Report : Displays all employee data in a neatly formatted table.
- Single Employee Report : Displays detailed information of a specific employee based on the entered NIP.

### c. Add Employee Data (CREATE)

Users can add new employee data by entering NIP, Name, Gender, Branch, Performance, and Absence.
Before saving, the program asks for confirmation (Y/N).

### d. Edit Employee Data (UPDATE)

Users can update specific fields of employee data by entering the employee’s NIP.
Editable fields include: Name, Gender, Branch, Performance, and Absence.
All updates require confirmation before being saved.

### e. Delete Employee Data (DELETE)

Employee data can be deleted based on NIP.
The program requests confirmation to prevent accidental deletion.

### f. Salary and Bonus Calculation

This feature calculates the total salary received by an employee based on:

- Base Salary : IDR 10,000,000
- Base Bonus : IDR 1,000,000

Performance Bonus:
- Performance A → 20% of base salary
- Performance B → 10% of base salary
- Performance C → No additional bonus

Attendance Penalty:
- Absence ≤ 4 days → No penalty
- Absence > 4 days:
  - Performance A/B → 5% of base salary penalty
  - Performance C → 10% of base salary penalty


The program displays a detailed breakdown are Base Salary, Performance Bonus, Penalty and Total Salary Received
