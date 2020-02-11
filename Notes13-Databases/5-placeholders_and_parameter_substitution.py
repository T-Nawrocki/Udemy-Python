# Using this program to do the mini challenge from the Placeholders and Parameter Substitution Lecture.
# ==================================================
# REQUIREMENTS:
#   Connect to contacts.sqlite
#   Ask user to enter a name
#   Retrieve and print the row for that name
# ==================================================

import sqlite3

db = sqlite3.connect("contacts.sqlite")

name_input = input("Please enter your name to see what details we've got for you: ")

query = "SELECT * FROM contacts WHERE name LIKE ?"  # use LIKE to make it case insensitive
cursor = db.cursor()
cursor.execute(query, (name_input,))  # Need to use (name_input,) because the argument must be a tuple with 1 element.

for row in cursor:
    print(row)

cursor.close()
db.close()
