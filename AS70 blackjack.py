import random
cards_list = ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'k', 'q', 'j']
count = 0
while True:
    if count == 21:
        print("Congratulations, you won!")
        break
    elif count > 21:
        print("bust")
        break
    user_input = input("hit or pass")
    if user_input.lower() == 'hit':
        card_drawn = random.choice(cards_list)
        print("you got", card_drawn)
        if card_drawn == 'a':
            if count < 10:
                count += 11
                continue
            count += 1
            continue
        if card_drawn == 'k' or card_drawn == 'q' or card_drawn == 'j':
            count += 10
            continue
        else:
            count += card_drawn
    else:
        break

if count < 21:
    print(21-count, "off getting bj")
