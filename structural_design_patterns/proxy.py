# Subject interface
class BankAccount:
    def withdraw(self, amount):
        pass


# Real subject
class ConcreteBankAccount(BankAccount):
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            print(f"Withdrawing {amount} from the account")
            self._balance -= amount
        else:
            print("Insufficient funds")


# Proxy
class BankAccountProxy(BankAccount):
    def __init__(self, balance):
        self._account = ConcreteBankAccount(balance)

    def withdraw(self, amount):
        if amount <= 1000:
            self._account.withdraw(amount)
        else:
            print("Withdrawal amount exceeds limit")


# Example usage
real_account = ConcreteBankAccount(5000)
real_account.withdraw(2000)  # Output: Withdrawing 2000 from the account
real_account.withdraw(6000)  # Output: Insufficient funds

proxy_account = BankAccountProxy(5000)
proxy_account.withdraw(500)  # Output: Withdrawing 500 from the account
proxy_account.withdraw(1500)  # Output: Withdrawal amount exceeds limit
