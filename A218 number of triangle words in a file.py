from math import sqrt

file_path = 'Script 3.txt'


def word_val(word):
    word_val_count = 0
    alphabets_l = list('abcdefghijklmnopqrstuvwxyz'.upper())
    for letter in word:
        word_val_count += alphabets_l.index(letter) + 1
    return word_val_count


def triangle(word):
    wv = word_val(word)
    a = 1
    b = 1
    c = (-2) * (wv)
    n1 = (-b + sqrt((b**2)-(4*a*c))) / (2*a)
    if n1 % 1 == 0:
        return True
    return False


count = 0
with open(file_path) as file:
    for line in file:
        words = line.split('","')
        words[0] = words[0][1:]
        words[-1] = words[-1][:-1]

    for word in words:
        if triangle(word):
            count += 1

print(count, "are triangle words")
