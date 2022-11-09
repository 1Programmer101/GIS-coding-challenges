free_var = None

num = input("Number:")
chars = list(num)
bcd_list = []

for char in chars:
    try:
        free_var = int(char)
        binary_val = ("{:b}".format(free_var))
        full_bin = ('0' * (4-len(binary_val))) + str(binary_val)
        bcd_list.append(full_bin)
    except:
        bcd_list.append(char)

print("".join(bcd_list))
