menu = "1) Add 2 numbers and display the result\n2) Subtract 2 numbers and display the result\n3) Multiply 2 numbers and display the result\n4) Divide 2 numbers and display the result\n"
print(menu)
choice = int(input("Enter selection: "))

match choice:
    case 1:
        x = int(input("First number to add: "))
        y = int(input("Second number to add: "))

        sum = x + y
        print(f"{x} + {y} = {sum}")

    case 2:
        x = int(input("First number to subtract from: "))
        y = int(input("Second number to subtract: "))

        diff = x - y
        print(f"{x} - {y} = {diff}")

    case 3:
        x = int(input("First number to multiply: "))
        y = int(input("Second number to multiply: "))

        product = x * y
        print(f"{x} * {y} = {product}")

    case 4:
        x = int(input("First number to be divided: "))
        y = int(input("Second number to divide: "))

        if (y == 0):
            print("Unable to divide by 0")
        else:
            quotient = x / y
            print(f"{x} + {y} = {quotient}")

print("Program complete.")