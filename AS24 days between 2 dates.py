import datetime
initial_date = input("Please enter the intitial date in format date/month/year:\n").split("/")
Final_date = input("Please enter the fianl date in format date/month/year:\n").split("/")
dayin, monthin, yearin= int(initial_date[0]), int(initial_date[1]), int(initial_date[2])
dayfin, monthfin, yearfin = int(Final_date[0]), int(Final_date[1]), int(Final_date[2])
x = datetime.datetime(yearfin, monthfin, dayfin) - datetime.datetime(yearin, monthin, dayin)
print(x)
