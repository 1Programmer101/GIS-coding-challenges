list_ = []
num = input("add in numbers seperated by a comma:").split(",")
for numbers in num:
    list_.append(int(numbers))
min_differences = []
min_val = abs(list_[1] - list_[0])
for elems in range(len(list_)):
    for compares in range(elems+1, len(list_)):
        if abs(list_[compares] - list_[elems]) < min_val:
            min_val = abs(list_[compares] - list_[elems])

print(min_val)
