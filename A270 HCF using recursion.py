def hcf(a,b):
    if b==0:
        return a
    else:
        print(a, b)
        return hcf(b, a%b)


num1, num2 = int(input("Num 1\n")), int(input("Num 2\n"))
print(hcf(num1, num2))
