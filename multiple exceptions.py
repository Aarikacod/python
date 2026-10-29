try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result= num1 / num2
    print("Result is", result)


except ZeroDivisionError:
    print("Division by zero is errror")


except ValueError:
    print("Please enter a valid number")