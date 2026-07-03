'''
2. Bank Account Management System
Develop a Python program to simulate a basic bank system.
Each account should have account number, account holder name, and balance.
The system must support deposit, withdrawal, balance enquiry, 
and prevent withdrawal if balance is insufficient.
'''

print("---------------------------------------------------")
print("WELCOME! to Dhrubo's Bank Management System :- ")
account_number = []
account_name = []
account_balance = []

while True:
    print("Bank Menu :"
          "\n1. Create Account"
          "\n2. Deposit Money"
          "\n3. Withdraw Money"
          "\n4. Check Balance"
          "\n5. Exit")
    choice = int(input("Enter Choice : "))
    print("---------------------------------------------------")
    # Create Account
    if choice == 1:
        acc_num = int(input("Enter New Account Number : "))
        while acc_num in account_number:
            print("Account already Exists, Please enter different number")
            acc_num = int(input("Enter New Account Number : "))
        acc_name = input("Enter Account Holder Name : ")
        acc_bal = int(input("Enter Initial Balance in Rupees: "))

        account_number.append(acc_num)
        account_name.append(acc_name)
        account_balance.append(acc_bal)

        print("\nAccount Created Succesfully")
        print("---------------------------------------------------")
    # Deposit Money
    elif choice == 2:
        num = int(input("Enter Account Number : "))
        if num in account_number:
            index = account_number.index(num)
            deposit = int(input("Enter Amount to be Deposit : "))
            account_balance[index] = account_balance[index] + deposit
            print("\nAmount Deposited Succcesfully")
            print("---------------------------------------------------")
        else:
            print("ACCOUNT NOT FOUND")
            print("---------------------------------------------------")
    # Withdraw Money
    elif choice == 3:
        num = int(input("Enter Account Number : "))
        if num in account_number:
            index = account_number.index(num)
            withdraw = int(input("Enter Amount to be Withdraw : "))
            if withdraw < account_balance[index]:
                account_balance[index] = account_balance[index] - withdraw
                print("\nAmount Withdrawal Succesfully")
                print("---------------------------------------------------")
            else:
                print("Insufficient Balance")
                print("---------------------------------------------------")
        else:
            print("ACCOUNT NOT FOUND")
            print("---------------------------------------------------")
    # Check Balance
    elif choice == 4:
        num = int(input("Enter Account Number : "))
        if num in account_number:
            index = account_number.index(num)
            balance = account_balance[index]
            name = account_name[index]
            print("Account Holder : ",name)
            print("Account Balance : ",balance)
            print("---------------------------------------------------")
        else:
            print("ACCOUNT NOT FOUND")
            print("---------------------------------------------------")
    elif choice == 5:
        print("Thanks for using 'Dhrubo's Bank Management System'.")
        n = int(input("Please Rate our service out of 10 : "))
        print("Thanks for Rating us")
        print("---------------------------------------------------")
        break
    else:
        print("INVALID INPUT !")
        print("---------------------------------------------------")

