def neat(num):
    sum = 0
    digits = list(str(num))
    for digit in digits:
        sum += int(digit)
    if num % sum == 0:
        return True
    return False

print('The neat numbers between 101 and 1000 are:')
for x in range(101, 1001):
    if neat(x):
        print(x, end=", ")
