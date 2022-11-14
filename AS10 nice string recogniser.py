# There are rules randomly made up to put a string under 'nice' section
# This includes rules such as the string containing atleast 3 vowels, has 2 same letter together, and the string not have 'xy', 'ab', 'cd', nor 'pq'

def nice(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    vowel_rule = double_letter_rule = succesive_letter_rule = False
    first_letter, second_letter = None, None
    for letter in string:
        if letter in vowels:
            vowels_count += 1
        first_letter = second_letter
        second_letter = letter
        if first_letter == second_letter:
            double_letter_rule = True

    for invalid_letter in ['ab', 'cd', 'pq', 'xy']:
        if invalid_letter in string:
            succesive_letter_rule = False
            break
        else:
            succesive_letter_rule = True


    if vowels_count >= 3:
        vowel_rule = True

    if vowel_rule and double_letter_rule and succesive_letter_rule:
        return True
    return False


string = input("String:")
if nice(string):
    print("Nice")
else:
    print("That aint nice")
