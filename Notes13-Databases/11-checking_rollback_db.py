import sqlite3
import pytz

# Sqlite3's Python library can automatically process certain data types (in this case, datetime data)
# however you need to let it know it should do this. We achieve this with the detect_types argument to the
# connection. Without this, the datetime data would simply be read as a string here.
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# Because we've declared that sqlite should detect and parse "decltypes", the datetime data in the time field is
# now available to python as a datetime object, as we'd expect (and can be converted to local time, etc, as usual).
for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print(f"{utc_time}\t{local_time}")

print("=" * 40)

# Shows local time using sqlite strftime function to convert to a string, as an alternative to the method used above.
# Note that the precision of the data is less here than using the native python methods above. This is why we've
# ordered by history.time, rather than by our converted datetime data, because that way we still get the benefits
# of a full 6 decimal places of precision for ordering, even if they're not represented here.
for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, "
                      "history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

db.close()

