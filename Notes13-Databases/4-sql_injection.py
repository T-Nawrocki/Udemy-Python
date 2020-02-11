# SQL injection is when someone inputs SQL commands into a field which is not intended to accept those commands.
# For example, you might have a user input their name, which is then updated to your database, however a user
# might be able to type a string containing SQL commands (eg "Tomek'; DROP TABLE contacts"), which can cause
# serious issues and security concerns.

# Now, often in sqlite this can be mitigated because the .execute() method actually can't execute more than one
# SQL command. However, the .executescript() method can execute more than one, and may often be very useful, so
# you can't just ignore it.

# Prepared statement are the usual solution to SQL injection. They consist of writing the command to be executed
# with placeholders (?) for the user inputted values.

import sqlite3

db = sqlite3.connect("contacts.sqlite")

# Oh no! A SQL injection attempt...
new_email = "newemail@update.com; DROP TABLE contacts"
name = "Tomek"

# This is our prepared statement. The ? are placeholders, which we will pass values to later.
# NB We do not need quotes around the ?, as the library's parameter substitution handles this for us.
# Some other database libraries will use different placeholder chars (eg %s or :1), so read documentation.
update_sql = "UPDATE contacts SET email = ? WHERE name = ?"

update_cursor = db.cursor()
# Execute the prepared statement, with a tuple of values to pass to the placeholders.
update_cursor.execute(update_sql, (new_email, name))

for row in db.execute("SELECT * FROM contacts"):
    print(row)
