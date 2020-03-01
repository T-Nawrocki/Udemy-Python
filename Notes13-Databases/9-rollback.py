# This program illustrates rolling back transactions in a banking app if an exception is raised


class Account:

    def __init__(self, name: str, opening_balance: float = 0.0):  # we've used type hints, and a default for balance
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}.")
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited.")
        else:
            print("Deposit failed: Cannot deposit negative amount or 0.")
        self.show_balance()
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0.0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn.")
        elif amount > self._balance:
            print("Withdrawal failed: Insufficient balance.")
        else:
            print("Withdrawal failed: cannot withdraw negative amount or 0.")
        self.show_balance()
        return self._balance

    def show_balance(self):
        print(f"Balance for account {self.name}: {self._balance}")


if __name__ == '__main__':
    tomek = Account("Tomek")
    tomek.deposit(10.10)
    tomek.deposit(90.90)
    tomek.withdraw(1)
    tomek.deposit(0)
    tomek.deposit(-41)
    tomek.withdraw(10000000)
    tomek.withdraw(0)
    tomek.show_balance()
