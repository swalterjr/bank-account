class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount): 
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")


    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

my_account = BankAccount("Shawn")

try:
    with open("balance.txt", "r") as file:
        my_account.balance = int(file.read())
except:
    my_account.balance = 0

while True:
    print("\n1: Deposit 2: Withdraw 3: Check balance 4: Quit")
    choice = input("What would you like to do?")

    if choice == "1":
        amount = int(input("How much to deposite? "))
        my_account.deposite(amount)
    elif choice == "2":
        amount = int(input("How much to withdraw? "))
        my_account.withdraw(amount)
    elif choice == "3":
        my_account.show_balance()
    elif choice == "4":
        with open("balance.txt", "w") as file:
            file.write(str(my_account.balance))
        print("Balance saved. Goodbye!")
        break
    else:
        print("Not a valid choice.")