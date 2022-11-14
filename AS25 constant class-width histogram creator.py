list_ = input("input numbers seperated by commas:\n").split(",")
for row in range(len(list_)):
    for col in range(int(list_[row])):
        print("*", end="")
    print("")
