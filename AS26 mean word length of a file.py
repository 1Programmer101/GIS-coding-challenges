words_count = letters_count = 0
with open('Script 2.txt') as file:
    for line in file:
        words = line.split()
        words_count += len(words)
        for letters in words:
            letters_count += len(letters)

print("average word length is", letters_count/words_count)
