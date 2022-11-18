list_ = [x for x in range(1, 112)]
print("Think of a number between 1 and 111 inclusive:\n")
while True:
    if len(list_) == 0:
        print("Wrong set of inputs. Please re-run this program and number MUST be in range 1 to 111. This must be an integer number")
        number = None
        break
    if len(list_) % 2 == 0:
        mid_ind = int(len(list_)/2) - 1
    else:
        mid_ind = int((len(list_)+1)/2) - 1
    if len(list_) == 1:
        number = list_[mid_ind]
        break
    mid = list_[mid_ind]
    print("H for number higher than",mid , "and L for lower. M if it is the number")
    a = input("")
    if a == 'L':
        list_ = list_[:mid_ind]
    elif a == 'H':
        list_ = list_[mid_ind+1:]
    else:
        number = list_[mid_ind]
        break

print("Number is", number)
