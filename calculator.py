while True:

    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Bye")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Answer:", a + b)

    if choice == 2:
        print("Answer:", a - b)

    if choice == 3:
        print("Answer:", a * b)

    if choice == 4:
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer:", a / b)
