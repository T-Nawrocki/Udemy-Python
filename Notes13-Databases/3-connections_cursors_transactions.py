import sqlite3

db = sqlite3.connect("contacts.sqlite")

# This portion of the code shows a couple different things.
# First of all, it shows that you can store a SQL command in a variable as a normal string (update_sql) and
# then use it later on (update_cursor.execute(update_sql)).
# Secondly, it shows using a cursor to update the database with the cursor.execute() call.
# Finally, it shows that a cursor can show how many rows match the command input using the .rowcount attribute.
update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.name = 'Tomek'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated")
# update_cursor.connection.commit()  # Use the cursor to commit the changes, not the connection, because we might
#                                      have multiple connections or have functions/objects which have a cursor
#                                      object but do not know about the connection itself, so this is the safer
#                                      and tidier way to achieve the exact same thing.
update_cursor.close()

# Can access rows from the database directly, without needing a cursor.
for row in db.execute("SELECT * FROM contacts"):
    print(row)

# When we first ran this, it did nothing, even though the code is correct! This is because in the previous
# program where we created the database, although we performed operations we did not COMMIT those operations.
# This is because SQLite, like other SQL implementations, wraps commands like INSERT INTO in something called
# a TRANSACTION. Essentially, a transaction is a commit consisting of one or more operations, which have been
# packaged together so that they can be rolled back together if needs be. So when we closed the database
# without committing the transaction in the last program, we essentially exited without saving, so the database
# has no records to be found by this program.

# For an example of transactions being used in practice—consider a banking app. When one account pays another,
# the database must be updated to reduce the balance of the first account and increase the balance of the second.
# Both of these updates must happen successfully, otherwise you end up with money disappearing or appearing
# without a destination or source. So the updates would be made to the database in your banking app, but will
# only be COMMITTED after confirming that both updates were successful and caused no errors. Otherwise, the
# whole transaction is rolled back, and you can take other actions (like presenting error messages or trying again).

# Now, with the db.commit() instruction in place in the last program, that program's changes are committed to
# the database, and this program correctly shows the data in that database.

db.close()

