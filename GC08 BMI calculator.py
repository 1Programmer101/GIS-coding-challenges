Weight = float(input("Please enter you weight in kilograms:\n"))
Height = float(input("Please enter you height in metres:\n"))
squared_height = Height**2
bmi = Weight/squared_height
if bmi < 18.5:
   print("Oopsies, you are underweight")
   print("You should gain some weight")
elif bmi >= 18.5 and bmi <25:
   print("Wow you are perfect weight for your height, you are fit")
elif bmi >= 25 and bmi < 30:
   print("Sorry, you are overweight, You should lose some weight")
elif bmi >= 30:
   print("ALERT: YOU ARE OBESE \n YOU MUST LOSE SOME WEIGHT TO BE HEALTHY")
print("Your BMI is", bmi)
if bmi < 18.5:
   weight_to_gain = (18.5-bmi)*squared_height
   print("You have to gain atleast", weight_to_gain, "kgs of weight to become fit")
elif bmi >=25:
   weight_to_lose = (25 - bmi)*(-1)*squared_height
   print("You have to lose atleast", weight_to_lose, "kgs of weight to become fit")
