string_ = input("string:")
string = list(string_)
count = 0
for char in string:
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        string[count] = char+'o'+char
    count += 1

print(''.join(string))
