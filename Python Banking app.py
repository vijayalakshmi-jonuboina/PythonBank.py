balance = 0.0
transactions = []

def deposit(amount):
    global balance

    balance += amount
    transactions.append(f'Deposited {amount}/-')
    print(f'{amount} deposited sucessfully\n')

def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficent Balance")
    else:
        balance = balance - amount
        transactions.append(f'withdraw{amount}/-')
        print(f'{amount} withdrawn sucessfully\n')

def checkBalance():
    print(f'Current Balance: {balance}\n') 

def transcationHistory():
    if not transactions:
        print("No Transcations yet")
    else:
        print('-----Transcations History-----')
        for t in transactions:
            print('-',t)
        deposists =sum(1 for t in transactions if 'Deposited' in t)
        withdraws =sum(1 for t in transactions if 'withdraw' in t)
        print(f'\nTotal Deposits: {deposists}')
        print(f'\nTotal withdraws: {withdraws}')

def menu():
    while True:
        print("-----PyBank Menu-----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        Choice =input('Enter Your Choice:')

        if Choice == '1':
            amount = float(input('Enter your amount to deposit:'))
            deposit(amount)
        elif Choice == '2':
            amount = float(input('Enter your amount to deposit:'))
            withdraw(amount)
        elif Choice == '3':
            checkBalance()
        elif Choice == '4': 
             transcationHistory()
        elif Choice =='5':
            print('Thank you for PYBank.Good Bye')
            break
        else:
            print('Invalid Choice')
menu()
