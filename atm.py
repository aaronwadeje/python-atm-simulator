balance = 500000
pin = "1234"

print("===== SIMPLE ATM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is: {balance} UGX")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print(f"Deposit successful!")
                print(f"New balance: {balance} UGX")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            else:
                balance -= amount
                print("Withdrawal successful!")
                print(f"Remaining balance: {balance} UGX")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")

else:
    print("Incorrect PIN. Access denied.")