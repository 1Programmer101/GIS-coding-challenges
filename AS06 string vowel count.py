strin = input("inputstring:\n")
count = 0
vowels = list("aeiou")
for characters in strin:
    if characters in vowels:
        count += 1
print("This has", count, 'vowels')
