class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, account_holder: str, balance: int) -> None:
        self.__account_holder = account_holder
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    @property
    def account_holder(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance

# TODO: Create two accounts
# TODO: Print the information using the mentioned format

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)
print(f"Alice's balance: ${alice_account.balance}")
print(f"Bob's balance: ${bob_account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")