import random
Total_lives = 10
The_number = random.randint(1, 101)
game_decider = 0


print("You have", Total_lives, "to guess a randomly generated number between 1-100\nGOOD LUCK :))\nI hope you enjoy this game!!\n_________")
while Total_lives >0:
   User_guess = int(input("please enter the number you guess is the number\n"))
   if User_guess == The_number:
       print("Congratulation, you won this round\nYOU ARE A REAL CHAMPION")
       print("You took", 10-Total_lives, "turns to guess and you had", Total_lives, "turns left")
       Total_lives = 0
       game_decider = 1
   if User_guess < The_number:
       print("The number is greater than the number you entered")
   if User_guess > The_number:
       print("The number is smaller/less than the number you entered")
   if User_guess != The_number:
       Total_lives -= 1
       print("__________________________________________________________________________________________")
       print("HEY DON’T WORRY.....YOU STILL GOT", Total_lives, "lives left")
       print("HAVE ANOTHER GO, DON’T GIVE UP")
   print("__________________________________________________________________________________________")

if Total_lives == 0 and game_decider == 0:
   print("Oopsies, you lost this game :(\nTHE NUMBER WAS", The_number)
   print("Run this code again to try again")
