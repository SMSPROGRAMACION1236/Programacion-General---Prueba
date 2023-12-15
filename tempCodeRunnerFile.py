
bank_account = int(input("Enter the money, you'll keep in this account bank: "))

account1=  bank_account *((1 + 0.04)**1)
print(f"The first year, you will pay: {round(account1, 2)}")
account2=  bank_account *((1 + 0.04)**2)
print(f"The second year, you will pay: {round(account2, 2)}")
account3=  bank_account *((1 + 0.04)**3)
print(f"The third year, you will pay: {round(account3, 2)}")