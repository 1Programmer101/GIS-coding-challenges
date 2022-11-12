import random
binary = [0, 1]
number = []
count = 0
for x in range(8):
    binary_dig = random.choice(binary)
    number.append(str(binary_dig))
    if binary_dig == 1:
        count += 1
full_num = ("".join(number))
print(full_num)
user_input = input("e for even parity and o for odd parity:\n")
if user_input == 'e' and count % 2 == 0:
    print("thats correct")
elif user_input == 'o' and count % 2 == 1:
    print("thats correct")
else:
    print("Thats wrong")
