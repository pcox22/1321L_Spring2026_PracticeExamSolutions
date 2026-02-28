size = int(input("Enter a number and we'll create shapes of that size: "))

print("Printing Rectangle: \n")
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

print("\nPrinting triangle: \n")

for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPrinting reverse triangle: \n")

for i in range(size):
    for j in range(size - i):
        print("*", end="")
    print()