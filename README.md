# Overview

My program creates a database in your computer's memory. The database is used to store information for a faux bike shop. Allow the user to create, modify, and delete the stock. The user can also have the stock read to them and have the results specified to list all information of items in stock meeting a given condition.

My purpose for writing this software was to demonstrate my understanding of SQL and the sqlite3 library for the python language and let me find out any areas that I might need improvement in.

[Module 3 Demo Video](https://youtu.be/jCQ6sI6y2qI)

# Relational Database

The database is created in the memory of the computer making the database get deleted after the program has ben run.

There is one table called stock.
It has an id column that accepts integer inputs, 
a model column that accepts only text, 
a name column that stores the name of the bike that stores the data as text, 
a column to store the quantity of the items in stock, 
and a column to store the price of the item.

# Development Environment

Visual Studio Code

Prgramming Language:
* Python

Libraries:
* sqlite3

# Useful Websites

* [Python.org](https://docs.python.org/3.8/library/sqlite3.html)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)

# Future Work

* Add other stores to the table and create stock for different stores
* Add more select statement options allowing for more than listing all information
* Create more information columns in the stock table