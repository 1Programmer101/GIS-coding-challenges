# Binomial theorem solver
# Challenge A259
from math import factorial


def ncr(n, r):
    n_f = factorial(n)
    r_f = factorial(r)
    nmr_f = factorial(n-r)
    return n_f / (r_f * nmr_f)


def return_expanded(term, n):
    letter_start = 0
    for char in term:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            break
        letter_start += 1
    letters = term[letter_start:]
    if letter_start != 0:
        numbers = term[:letter_start]
    else:
        numbers = 1
    exp_let = []
    for letter in letters:
        exp_let.append(letter+'^'+str(n))
    exp_let = " ".join(exp_let)
    if int(n) == 0:
        exp_let = ""
    return int(numbers)**n, exp_let


print("in format (a+b)^n")
binomial = input("")
a = binomial[1:(binomial.index('+'))]
b = binomial[(binomial.index('+') + 1):binomial.index(')')]
n = int(binomial[(binomial.index('^'))+1:])

int_a = False
int_b = False
try:
    float(a)
    int_a = True
    float(b)
    int_b = True
except:
    pass


r = 0
end = n
while r != end+1:
    if int_a and int_b:
        print((ncr(n, r) * (float(a) ** (n-r)) * (float(b)**r)), end="")
    elif int_a:
        num, letters = return_expanded(b, r)
        print((str(ncr(n, r) * (float(a) ** (n - r)) * num) + letters), end=" + ")
    elif int_b:
        num, letters = return_expanded(a, r)
        print((str(ncr(n, r) * (float(b) ** (n - r)) * num) + letters), end=" + ")
    else:
        num1, letters1 = return_expanded(a, (n-r))
        num2, letters2 = return_expanded(b, r)
        print((str(ncr(n, r) * num1 * num2) + letters1 + letters2), end=" + ")
    r = r + 1
