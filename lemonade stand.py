print("Hello, {name}! Welcome to my lemonade stand!")
total = 0
def calculate_total(price,quantity):
   total = price * quantity
   return total


def calculate_change(amount_paid , total_cost):
    change = amount_paid- total_cost
    return change


def print_recipt(name , quantity , price , total , paid , change):


     name = input("Enter your name:")
     greet_customer (name)

     price = 20
     quantity = int(input("How many cups of lemonade would you like ?"))


     total = calculate_total (price,quantity)
     print("Total")


paid = float(input("Enter the amount you pay:"))


if paid >= total:
    change = calculate_change (paid,total)
    


else:
    print("Sorry,the payment is insufficient")
    print("You still owe {total-paid:.}")


