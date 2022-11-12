import random

def bin_add(a, b):
    sum = bin(int(a, 2) + int(b, 2))
    return (sum[2:])

denary = random.randint(-127, 127)
print("Denary number is", denary)
negative = None
if str(denary)[0] == '-':
    negative = True
    denary = abs(denary)
else:
    negative = False

binary = "{:b}".format(denary)
binary = ((8-len(binary))*'0') + binary
list_bin = list(binary)

for indexes in range(len(list_bin)):
    if list_bin[indexes] == '0':
        list_bin[indexes] = '1'
    else:
        list_bin[indexes] = '0'

if negative:
    list_bin[0] = '1'
else:
    list_bin[0] = '0'

ones_comp = ''.join(list_bin)

twos_comp = (bin_add(ones_comp, '1'))
twos_comp = ((8-len(twos_comp))*'0') + twos_comp

print("Find the 2s complement in 8-bit format:")
if input("") == twos_comp:
    print("Thats the right answer. Congrats!")
else:
    print("Wrong answer")
    print("The right answer was", twos_comp)

print("\nsteps are:")
print("Binary value is", binary)
print("Ones complement is", ones_comp)
print("Hence, adding 1 to this gives", twos_comp)
