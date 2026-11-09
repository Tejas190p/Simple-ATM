print("===== MINI ATM =====")

balance = 1000
pin = input("Enter PIN: ")

if pin == "1234":

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter amount: "))
            balance = balance + amount
            print("Deposit successful!")
            print("Balance:", balance)

        elif choice == "3":
            amount = int(input("Enter amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Balance:", balance)
            else:
                print("Not enough balance!")

        elif choice == "4":
            print("Thank you! 👋")
            break

        else:
            print("Invalid choice!")

else:
    print("Wrong PIN! 🚫")
    