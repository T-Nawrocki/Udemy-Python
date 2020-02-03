# ENCAPSULATION is an important concept in OOP.
# It is the idea that objects contain the data, and the methods which act on that data,
# and do not expose the actual implementation of the data and methods to outside interaction.

# This is not the only way to achieve encapsulation.
# Other approaches have included encapsulating within modules, rather than objects.
# Python can accommodate both approaches (as we saw when using the pytz module for timezones, for example)

import datetime
import pytz


class Account(object):
    """ A simple bank account Class with balance """

    # Because this method does not actually use self anywhere in the definition,
    # IntelliJ recommends that it be implemented as a static method.
    # Static methods are shared by all instances of a class, in the same way class variables are shared.
    # Static methods are created by removing the self parameter and adding @staticmethod before the definition
    @staticmethod
    def _current_time():  # remember, by convention, names starting with _ are treated as non-public
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # We've previously called __init__ a constructor. This is not strictly true.
    # In the new Python class creation process (as of Python 2.2), there are two steps:
    # 1.    The first method to be called when an instance of the class is created is __new__.
    #       This takes care of the actual creation of the instance (so this is the true constructor).
    #       __new__ generally does not need to be explicitly defined or called,
    #       except when creating certain types of subclasses to a class.
    # 2.    The second method to be called is __init__.
    #       This customises the new instance by giving values to the instance attributes, for example.
    # Python 3 only has the new-style classes, but versions between 2.2 and 3 have both.
    # We will look at the old-style classes briefly later on.
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), self.balance)]
        print(f"Account created: name = {self.name}; balance = {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # append tuple containing utc localised datetime and amount to transaction list
            # could call _current_time() on self instead, but result is the same and performance is slightly worse
            # because python has to load the instance and class, not just class, so generally do it this way
            self.transaction_list.append((Account._current_time(), amount))
            print(f"{amount} deposited into account {self.name}.")
            self.show_balance()

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                # append tuple containing utc localised datetime and negative amount to transaction list
                self.transaction_list.append((Account._current_time(), -amount))
                print(f"{amount} withdrawn from account {self.name}.")
                self.show_balance()
            else:
                print(f"Attempted to withdraw {amount} from account {self.name}, but funds insufficient.")
                self.show_balance()

    def show_balance(self):
        print(f"Balance = {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            print(f"{date.astimezone()}: {amount} (balance = {self.balance})")


if __name__ == '__main__':

    tomek = Account("Tomek", 0)
    tomek.deposit(1000)
    tomek.withdraw(500)
    tomek.withdraw(5000)
    tomek.show_transactions()

    print("="*40)

    jen = Account("Jen", 800)
    jen.deposit(100)
    jen.withdraw(200)
    jen.show_transactions()
