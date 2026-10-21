CLI Expense Tracker
A command-line expense tracking application built with Python. It allows users to record daily expenses, view their spending history, and generate expense summaries.
Features

Add expenses with an amount, category, description, and date.
View all recorded expenses.
Calculate total expenses and monthly spending.
Summarize spending by category.
Save and load expense records using JSON.
Validate expense amounts and category input.

Technologies Used

Python 3
JSON
pathlib
datetime

Requirements

Python 3.10 or later.

How to Run

Download or clone this repository.
Open a terminal in the project folder.
Run:

python main.py

Usage
When the application starts, choose one of the following options:

Add Expense — Record a new expense.
View Expenses — Display saved expenses.
Show Summary — View total spending, monthly expenses, and spending by category.
Exit — Close the application.

Expense records are stored in expenses.json and loaded automatically when the application starts again.
Testing
The application was tested for:

Adding expenses.
Viewing saved expenses.
Calculating spending summaries.
Preserving expense records after restarting the application.

Project Purpose
This project demonstrates Python fundamentals, functions, input validation, file handling, JSON persistence, and basic data summarization.
Internship
Completed as part of the Elevvo Internship program.
