initial_bal = 1000
withdraw = float(input("How much would you like to withdraw?\n"))
if withdraw % 5 == 0 and initial_bal >= (withdraw + 0.5):
    print("Congrats, you have succesfully withrawn", withdraw)
elif withdraw % 5 != 0:
    print("The amount you want to withdraw has to be a multiple of 5")
else:
    print("Not enough cash in account")
    print("Account has", initial_bal)
