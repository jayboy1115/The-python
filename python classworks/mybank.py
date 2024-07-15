name = input("Enter your name: ")
print(f"Welcome to Johnson Kolo Bank, {name}!")

balance = 0

while True:
    alphabet = input("Enter D to deposit, E to withdraw, or F to check balance: ").upper()

    if alphabet == 'D':
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
        print(f"Deposit successful! Your new balance is {balance}")

    elif alphabet == 'E':
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw > balance:
            print("Insufficient funds!")
        else:
            balance -= withdraw
            print(f"Withdrawal successful! Your new balance is {balance}")

    elif alphabet == 'F':
        print(f"Your current balance is {balance}")

    else:
        print("Invalid input! Please try again.")

     

