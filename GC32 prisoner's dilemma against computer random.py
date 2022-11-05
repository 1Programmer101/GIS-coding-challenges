import random
choices = ["", "char"]
comp = random.choice(choices)
user_choice = input("Either confess something or stay silent by pressing enter and not typing anything:\n")
if user_choice == "" and comp == "":
    print("Prison punishment for a year")
    print("Your partner stayed silent")
elif user_choice == "" and comp == "char":
    print("Prison punishment for 20 years")
    print("Your parner confessed and has been released")
elif comp == "" and len(user_choice) > 0:
    print("You get released. No punishment")
    print("Your parner decided to stay silent")
else:
    print("Prison punishment for 5 years")
    print("Both of you confessed")
