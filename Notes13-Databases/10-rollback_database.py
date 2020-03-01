# Building on the code from the last exercise, this program stores the data for our Account class in a database

import sqlite3
import pytz
import datetime

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history "
           "(time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
# Note how the PRIMARY KEY is defined separately in this second command.
# This is called a "composite key", which means that no two records can have the same time AND the same account
# (although they can still have the same time OR the same account)

# Another thing to note is that including the balance in the accounts table breaks database Normalisation rules
# (remember that these are broadly speaking database style guides for producing easily maintainable/clean databases).
# In this case, the balance is unnecessarily dependent on the transactions table—we could remove the balance field
# entirely and replace it by summing the transactions in the transaction table. However, when your database gets
# much larger and has a very long transactions table, calculating the account balance this way every time you need
# it could cause performance issues. So you will often see examples like this where the usual rules for database
# normalisation are broken for the sake of improved performance. A real financial application might run an operation
# during quiet times to compare the values in the balance field with the transactions table, to keep them in line.

# The python sqlite3 library supports datetime values and will automatically convert data to datetime
# values when we read/write our timestamp values. However, we need to tell it to do that, which we will get to later.

db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, "
           "history.account, "
           "history.amount "
           "FROM history ORDER BY history.time")


class Account:

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: int = 0):  # we've used type hints, and a default for balance
        # Run a simple select query to find an account with the instance name
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        # If we found an account which matches the query, instance name and balance are taken from that account record
        if row:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}.")

        # If not, create a new record by inserting the name/balance values into the accounts table,
        # committing the changes immediately to make sure they're actually reflected in the database.
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}.")
        self.show_balance()

    def deposit(self, amount: int) -> int:
        if amount > 0:
            self._save_update(amount)
            print(f"{amount/100} deposited.")
        else:
            print("Deposit failed: Cannot deposit negative amount or 0.")
        self.show_balance()
        return self._balance

    def withdraw(self, amount: int) -> int:

        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print(f"{amount/100} withdrawn.")
        elif amount > self._balance:
            print("Withdrawal failed: Insufficient balance.")
        else:
            print("Withdrawal failed: cannot withdraw negative amount or 0.")
        self.show_balance()
        return self._balance

    def show_balance(self):
        print(f"Balance for account {self.name}: {self._balance/100}")

    def _save_update(self, amount):
        new_balance = self._balance + amount
        update_time = Account._current_time()

        # Try/except/else prevents committing an invalid transaction.
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE(name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES (?, ?, ?)", (update_time, self.name, amount))
        except sqlite3.Error:
            # need to rollback even though commit is never called so that we don't accidentally commit the changes later
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance


if __name__ == '__main__':
    tomek = Account("Tomek")
    jen = Account("Jen")
    herbert = Account("Herbert")
    goose = Account("Goose")

    tomek.deposit(1000)
    tomek.withdraw(500)
    jen.deposit(50000)
    jen.withdraw(10000000)
    jen.withdraw(100)
    herbert.deposit(50)

db.close()