
from collections import deque

queue = deque()

# Add customers
queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")
queue.append("Customer 4")

print("Grocery Billing Queue:")
print(queue)

# Serve customers
while queue:
    customer = queue.popleft()
    print("Billing:", customer)

print("All customers have been served!")



from collections import deque

queue = deque()

# Customer name and bill amount
queue.append(("Aarav", 250))
queue.append(("Riya", 430))
queue.append(("Kabir", 180))
queue.append(("Anaya", 520))

print("Grocery Billing Queue\n")

while queue:
    customer, amount = queue.popleft()

    print("Customer:", customer)
    print("Bill Amount: ₹", amount)
    print("Payment successful!")
    print("--------------------")

print("Queue is empty.")



from collections import deque

queue = deque()

n = int(input("Enter number of customers: "))

for i in range(n):
    name = input("Enter customer name: ")
    amount = float(input("Enter bill amount: ₹"))
    queue.append((name, amount))

print("\n--- Grocery Billing ---")

while queue:
    name, amount = queue.popleft()
    print("Customer:", name)
    print("Bill: ₹", amount)
    print("Payment completed!\n")

print("All customers have been billed.")




