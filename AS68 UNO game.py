import random
from time import sleep as wait

# Initial cards
Cards_drawn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'skip', 'rev', 'dr2']
No_col = ['wild', 'dr4']
Colours = ['r', 'b', 'g', 'y']
all_cards = Cards_drawn+No_col

user_drawn_cards = []
computer_drawn_cards = []
colour_now, card_now = random.choice(Colours), random.choice(Cards_drawn[0:10])
last_card = card_now+colour_now

Have_card = False
comp_turn = True
computer_pass = False

print("Starting card is", last_card)
def draw_random(num, list_):
    for crs in range(num):
        card = random.choice(all_cards)
        if card in No_col:
            list_.append(card)
        else:
            colour = random.choice(Colours)
            list_.append(card+colour)


def computer_play():
    global colour_now, card_now, last_card, Have_card, comp_turn, computer_pass
    Have_card = False
    for elems in computer_drawn_cards:
        if elems[-1] == colour_now or elems[0:-1] == card_now or elems in No_col:
            card = elems
            Have_card = True
            last_card = card
            break
    if Have_card:
        computer_drawn_cards.remove(card)
        if card in No_col:
            colour_now = random.choice(Colours)
            card_now = None
        else:
            colour_now, card_now = card[-1], card[0:-1]
    else:
        draw_random(1, computer_drawn_cards)
        print("Computer passed")
        comp_turn = False
        computer_pass = True


def validate_card(card):
    if card == 'pass':
        return True
    if card not in user_drawn_cards:
        return False
    if card in No_col:
        return True
    if card[-1] == colour_now:
        return True
    if card[0:-1] == card_now:
        return True

    return False


draw_random(7, user_drawn_cards)
draw_random(7, computer_drawn_cards)

while len(user_drawn_cards) != 0 and len(computer_drawn_cards) != 0:
    print("You have", len(user_drawn_cards), 'cards while the computer has', len(computer_drawn_cards), 'cards')
    if comp_turn:
        computer_play()
        if not computer_pass:
            print("Computer played", last_card)
        else:
            computer_pass = False
        comp_turn = False
        # print("Computer has", computer_drawn_cards)
        # print(last_card, colour_now, card_now)
        if last_card[0:-1] == 'dr2':
            draw_random(2, user_drawn_cards)
            colour_now, card_now = last_card[-1], 'dr2'
        elif last_card == 'dr4':
            draw_random(4, user_drawn_cards)
            colour_now, card_now = random.choice(Colours), 'dr4'
            print("Colour changes to", colour_now)
        elif last_card[0:-1] == 'skip':
            comp_turn = True
            colour_now, card_now = last_card[-1], 'skip'
        elif last_card == 'wild':
            colour_now, card_now = random.choice(Colours), None
            print("Colour changes to", colour_now)
        elif last_card[0:-1] == 'rev':
            comp_turn = True
        else:
            colour_now, card_now = last_card[1], last_card[0]

    if not comp_turn:
        print("You have: ", end="")
        [print(x, end=", ") for x in user_drawn_cards]
        print("")
        while True:
            user_card = input("What card do you want to play? or type 'pass'\n")
            if validate_card(user_card):
                if user_card != 'pass':
                    last_card = user_card
                comp_turn = True
                break
            else:
                print("YOU CANT PLAY THAT!")
        if user_card == 'pass':
            draw_random(1, user_drawn_cards)
        elif user_card[0:-1] == 'dr2':
            draw_random(2, computer_drawn_cards)
            colour_now, card_now = user_card[-1], 'dr2'
            user_drawn_cards.remove(user_card)
        elif user_card == 'dr4':
            draw_random(4, computer_drawn_cards)
            colour_now, card_now = input("what colour do you want to change to? (rgby)"), 'dr4'
            user_drawn_cards.remove(user_card)
        elif user_card[0:-1] == 'skip':
            comp_turn = False
            colour_now, card_now = user_card[-1], 'skip'
            user_drawn_cards.remove(user_card)
        elif user_card == 'wild':
            colour_now, card_now = input("what colour do you want to change to? (rgby)"), None
            user_drawn_cards.remove(user_card)
        elif user_card[0:-1] == 'rev':
            comp_turn = False
            user_drawn_cards.remove(user_card)
        else:
            colour_now, card_now = user_card[1], user_card[0]
            user_drawn_cards.remove(user_card)

if len(user_drawn_cards) == 0:
    print("CONGRATULATIONS!!!")
    wait(2)
    print("YOU WONT THE ULTIMATE UNO GAME AGAINST THE SUPER SMART COMPUTER!!!")
    wait(1)
    print("True genius")
else:
    print("Such a loser, couldnt even win against a computer")
    wait(2)
    print("be more hardworking")
