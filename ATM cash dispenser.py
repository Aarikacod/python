print("=== ATM cash dispenser ===")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0 
total_dispensed = 0 

serving = True 
while serving: 
    name = input("Enter customer name")
    amount = input ("Enter your amount")
    if amount <= "0" :
        print("Invalid number. Please enter a positive number")
    print("amoumt unit and name")

    remaining = amount
    i = 1
    while i< 4:
        if i == 1: value = 100
        if i == 2: value = 50
        if i == 3: value = 20
        if i == 4: value = 5

        i = i +1
    print("value,amount")

        
