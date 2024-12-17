import calculator

def test_calculator():
    print("Simple Calculator")
    print("---------------------")

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = calculator.add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = calculator.subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = calculator.multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        try:
            result = calculator.divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid operator. Please try again.")

    print("---------------------")

if __name__ == "__main__":
    test_calculator()
