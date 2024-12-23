def validate_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def test_calculator(a, b):
    a_valid = validate_number(a)
    b_valid = validate_number(b)

    if a_valid is None or b_valid is None:
        print(f"Invalid input detected: '{a}' or '{b}' is not a number.")
        print("---------------------")
        return

    a, b = a_valid, b_valid
    print("---------------------")
    print(f"Adding ({a} + {b})")
    print(f"{a} + {b} = {a + b}")
    print("---------------------")
    print(f"Subtracting ({a} - {b})")
    print(f"{a} - {b} = {a - b}")
    print("---------------------")
    print(f"Multiplying ({a} * {b})")
    print(f"{a} * {b} = {a * b}")
    print("---------------------")
    if b != 0:
        print(f"Dividing ({a} / {b})")
        print(f"{a} / {b} = {a / b}")
    else:
        print(f"Dividing ({a} / {b})")
        print("Error! Division by zero.")
    print("---------------------")

def get_input():
    try:
        a = input("Enter first value: ").strip()
        b = input("Enter second value: ").strip()
        test_calculator(a, b)
        
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    get_input()
    cont = input("Do you want to test another calculation? (y/n): ").strip().lower()
    if cont != 'y':
        print("Exiting the calculator.")
        break