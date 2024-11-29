import random

# Step 1: Create a list of 12 random integers
random_integers = [random.randint(-100, 100) for _ in range(12)]

# Step 2: Check each number in the list
for number in random_integers:
    # i. Check if it’s even or odd
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    # ii. Check if it’s positive or negative
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")

    # iii. Check if it matches a specific number you have in mind
    specific_number = 42  
    if number == specific_number:
        print(f"{number} matches the specific number {specific_number}")
    else:
        print(f"{number} does not match the specific number {specific_number}")
    
    print()  

# Step 3: Bonus Activity - Calculator Simulator
# Take 3 inputs
var1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
var2 = float(input("Enter the second number: "))

# Step 4: Calculate the result based on the operator
if operator == "+":
    result = var1 + var2
elif operator == "-":
    result = var1 - var2
elif operator == "*":
    result = var1 * var2
elif operator == "/":
    if var2 != 0:
        result = var1 / var2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operator"

print(f"Result: {result}")

# Step 5: Accumulate calculations if the user wants to keep adding to the result
accumulated_result = result if isinstance(result, (int, float)) else 0
while True:
    reset = input("Do you want to reset (C for reset, any key to continue): ").strip().upper()
    if reset == 'C':
        accumulated_result = 0
        print("Accumulator reset to 0.")
    else:
        var1 = float(input("Enter the next number: "))
        operator = input("Enter the next operator (+, -, *, /): ")
        var2 = float(input("Enter the next number: "))

        # Calculate and accumulate the result
        if operator == "+":
            accumulated_result += var1 + var2
        elif operator == "-":
            accumulated_result += var1 - var2
        elif operator == "*":
            accumulated_result += var1 * var2
        elif operator == "/":
            if var2 != 0:
                accumulated_result += var1 / var2
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operator")
        
        print(f"Current accumulated result: {accumulated_result}")