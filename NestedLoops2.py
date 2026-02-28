size = int(input("Enter a size and we will make shapes using it: "))

print("\nPrinting Rectangle: ")
for i in range(1, size + 1):
    for j in range(size, 0, -1):
        print(j, end="")
    print()


print("\nPrinting Triangle: ")
for i in range(1, size + 1):
    for j in range(size, size - i, -1):
        print(j, end="")
    print()

print("\nPrinting Upside-Down Triangle: ")
for i in range(size, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()