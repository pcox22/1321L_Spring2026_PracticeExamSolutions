def take_sum(x, y):
    return (x + y)

def take_difference(x, y):
    return (x - y)

def take_product(x, y):
    return (x * y)

def take_quotient(x, y):
    if y == 0:
        return "Impossible: cannot divide by 0!"
    return (x / y)


while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Select operation to perform: ")
    print("1) Add numbers")
    print("2) Subtract numbers")
    print("3) Multiply numbers")
    print("4) Divide numbers")
    print("0) Quit Program")
    choice = int(input())

    match choice:
        case 1:
            result = take_sum(num1, num2)
            print(f"{num1} + {num2} = {result}")
        case 2:
            result = take_difference(num1, num2)
            print(f"{num1} - {num2} = {result}")
        case 3:
            result = take_product(num1, num2)
            print(f"{num1} * {num2} = {result}")
        case 4:
            result = take_quotient(num1, num2)
            print(f"{num1} / {num2} = {result}")
        case 0:
            break
        case _:
            print("Invalid Option! Try again.")
    print()

print("Shutting down...")