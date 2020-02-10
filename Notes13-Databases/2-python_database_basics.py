import sqlite3

# In general, SQLite doesn't care what you call your database, and we've used .db previously because that's a fairly
# standard database extension. However, here we're using .sqlite because _______
db = sqlite3.connect("contacts.sqlite")

# Semicolons aren't needed in the sqlite3 module—one is implicitly added to the end of each command string when
# the command is interpreted. The only time you'd need a semicolon is where a single string contains more than one
# SQL command. However, in general it's a good idea to avoid semicolons here unless you know you need them, because
# that way you won't run into trouble if, for example, you write a SELECT command and later need to concatenate a
# WHERE statement to the end of it.
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Tomek', 1234567890, 'tomek@website.com')")
db.execute("INSERT INTO contacts VALUES('Jen', 987654321, 'jen@email.website')")

# A cursor is a GENERATOR. This is an iterable object type we haven't dealt with much yet but what it does is
# generate the next value each time it's used, thus saving on memory compared to an object that inherently contains
# every value in the sequence (like a list). Cursors generate the rows of the table as a tuple.
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())  # .fetchall() returns a list containing tuples of each value the cursor would return

# An alternative way to do the same thing.
# In this case, it won't actually do anything beacause our generator has already iterated through the entire database
# and reached the end, so when it tries to move to the next row there's nothing to find and it returns nothing.
for row in cursor:
    print(row)

cursor.close()  # Closes the cursor, clearing it from memory.
#                 To use it again, we'd need to recreate it with the same query.

db.commit()  # Saves changes to the database—see notes on the next program for full explanation.
db.close()  # Need to end by closing off our database connection.
