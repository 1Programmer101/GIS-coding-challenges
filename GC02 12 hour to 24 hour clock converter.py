twelve_hour_time = input("please enter a time in the 12 hour time zone if you want to convert it to 24 hr clock time\nPlease split the hours and minutes by a colon(:)\n")
splited_time_version = twelve_hour_time.split(':')
am_or_pm = input("Is this time A.M. or P.M.\tplease enter am or pm for your input for this programme to work\n")
if int(splited_time_version[0]) > 12 or int(splited_time_version[1]) >= 60:
   print("please enter a valid 12 hr time zone number")
elif twelve_hour_time == "12:00" and am_or_pm == "am":
   print("The 24 hour clock time is 00:00")
elif am_or_pm == 'pm':
   twenty_hour_time_hours = int(splited_time_version[0]) + 12
   twenty_hour_time_minutes = splited_time_version[1]
   print("The 24 hour clock time is ", twenty_hour_time_hours, ':', twenty_hour_time_minutes, sep="")
elif am_or_pm == 'am':
   print("The 24 hour clock time is ", twelve_hour_time)
else:
   print("Add a proper time/am/pm:::\n A few examples of the time are::\n1:00, 7:49, 12:00\nAnd a please just write am or pm for the time range")
