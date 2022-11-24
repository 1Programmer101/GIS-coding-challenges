try:
   number_of_levels = int(input("How many levels do you want for this pyramid\n________________________\n"))
   for x in range(number_of_levels):
       aa = 2 * x
       for y in range(aa + 1):
           print('X', end="")
       print("")
except:
   print("PLEASE ENTER AN INTEGER")
