base = int(input("Enter the base: "))
power = int(input("Enter the power: "))

result = base ** power

print("Answer:", result)

def power_calculator(base, power):
    return base ** power

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))

print("Answer:", power_calculator(base, power))


while True:
    base = int(input("Enter the base: "))
    power = int(input("Enter the power: "))

    result = base ** power
    print("Answer:", result)

    again = input("Do you want to calculate again? (yes/no): ")

    if again.lower() == "no":
        print("Thank you!")
        break