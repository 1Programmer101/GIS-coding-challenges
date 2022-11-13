def make_it_laugh(string):
    list_string = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char_ind in range(len(list_string)):
        if list_string[char_ind] in vowels:
            list_string[char_ind] = 'haha'
    updated = "".join(list_string)
    print(updated)
