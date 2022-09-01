print("Please input all the numbers for the length of each row in the histogram")
print("Seperate your numbers by using a comma followed by one space:")
numbers = input("").split(", ")
print(type(numbers))
for rows in numbers:
    for length in range(int(rows)):
        print("*", end="")
    print()
