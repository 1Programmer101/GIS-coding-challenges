# Fibonacci series
a = 1
b = 1
print("1, 1, ", end="")
for x in range(98):
   c = a+b
   print(c, end = ", ")
   a = b
   b = c
