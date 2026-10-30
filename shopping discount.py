
print("===== SHOPPING DISCOUNT COUNTER =====")

name = input("Enter customer name: ")
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    rate = 25
elif amount >= 3000:
    rate = 20
elif amount >= 1000:
    rate = 10
else:
    rate = 0

discount = amount * rate / 100
final_amount = amount - discount

print("========== BILL ==========")
print("Customer Name:", name)
print("Shopping Amount: Rs.", amount)
print("Discount Rate:", rate, "%")
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
print("==========================")
print("Thank you for shopping!")
