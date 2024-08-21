def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def modulus_numbers(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Modulus by zero is not allowed."

def power_numbers(a, b):
    return a ** b

def simple_calculator():
    print("Simple Calculator - Let's do some math!")
    
    # Input with error handling for non-numeric values
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        return "Oops! That's not a valid number. Please enter numeric values."

    print("\nWhat operation would you like to perform?")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")
    print("5: Modulus (%)")
    print("6: Power (^)")

    # User operation choice with validation
    operation = input("Choose an operation by entering the number (1/2/3/4/5/6): ")

    if operation == '1':
        result = add_numbers(num1, num2)
        op_symbol = "+"
    elif operation == '2':
        result = subtract_numbers(num1, num2)
        op_symbol = "-"
    elif operation == '3':
        result = multiply_numbers(num1, num2)
        op_symbol = "*"
    elif operation == '4':
        result = divide_numbers(num1, num2)
        op_symbol = "/"
    elif operation == '5':
        result = modulus_numbers(num1, num2)
        op_symbol = "%"
    elif operation == '6':
        result = power_numbers(num1, num2)
        op_symbol = "^"
    else:
        return "Invalid selection! Please choose a valid operation."

    # Custom message for negative results
    if isinstance(result, str):  # Checking if result is an error message
        return result
    elif result < 0:
        return f"\nResult: {num1} {op_symbol} {num2} = {result} (Negative result!)"
    else:
        return f"\nResult: {num1} {op_symbol} {num2} = {result}"

# Run the calculator if executed as the main script
if __name__ == "__main__":
    print(simple_calculator())
