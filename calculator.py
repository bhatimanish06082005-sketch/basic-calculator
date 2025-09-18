try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("CHOOSE OPERATION TO PERFORM:\n"
          "1. ADDITION\n"
          "2. SUBTRACTION\n"
          "3. DIVISION\n"
          "4. MULTIPLICATION\n")

    cal = input("Enter operation name: ").strip().upper()

    if cal == "ADDITION":
        ans = num1 + num2
    elif cal == "SUBTRACTION":
        ans = num1 - num2
    elif cal == "DIVISION":
        if num2 == 0:
            print("Cannot divide by zero!")
            ans = None
        else:
            ans = num1 / num2
    elif cal == "MULTIPLICATION":
        ans = num1 * num2
    else:
        print("Invalid operation!")
        ans = None

    if ans is not None:
        print(f"The answer is: {ans}")

except ValueError:
    print("INVALID INPUT! Please enter valid numbers.")
