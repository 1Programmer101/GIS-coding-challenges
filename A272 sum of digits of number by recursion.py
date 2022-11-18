def Sum(num):
    if num == 0:
        return num
    else:
        print(round(num/10, 5), round(num%10, 5))
        return Sum(num//10) + (num % 10)

print(Sum(155))
