from datetime import datetime, timedelta, date

[30,30,31,30,30,31,30,30,31,30,30,31]

# taking input as the current date
# today() method is supported by date
# class in datetime module
Begindatestring = date(2021,3,20)

# print begin date
print("Beginning date")
print(Begindatestring)

# calculating end date by adding 4 days
Enddate = Begindatestring + timedelta(days=4)

# printing end date
print("Ending date")
print(Enddate)

day_of_year = datetime.now().timetuple().tm_yday
print("\nDay of year: ", day_of_year, "\n")

new_day_of_year = Begindatestring.timetuple().tm_yday
print("\nDay of year: ", new_day_of_year, "\n")

value = datetime.today().weekday()

week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
scripture_week = ["2nd Day","3rd Day","4th Day","5th Day","6th Day","7th Day","1st Day"]

print(week[value])
print(scripture_week[value])
