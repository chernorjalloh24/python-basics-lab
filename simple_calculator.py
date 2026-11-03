num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask the user to choose an operation
operator = input("Choose an operation (+, -, *, /): ")

# Perform the calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator.")
    result = None

# Display the result
if result is not None:
    print(f"{num1} {operator} {num2} = {result:g}")


