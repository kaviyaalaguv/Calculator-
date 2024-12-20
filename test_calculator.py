def test_calculator(a, b):
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


test_calculator(4, 5)
