def calculate_change (paid,price):
    change = paid-price 
    return change


snack_price = 25
print("===== snack vending machine =====")
print("This snack cost {snack_price} units")
print("Accepted coins: 1, 5, 10, 25")


total_inserted = 0 
coins_inserted = 0 


while True:
    coin = int(input("Insert a coin(1,5,10 or 25:)"))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again ")
        continue


    if total_inserted >= snack_price:
        print("Enough money inserted")
        break

