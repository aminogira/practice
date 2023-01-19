import calendar

date_input = input("")
month, day, year = map(int, date_input.split(" "))

day_name = calendar.day_name[calendar.weekday(year, month, day)]
print(day_name.upper())



print (calendar.TextCalendar(firstweekday=6).formatyear(2023))


import datetime

date_input = input("Enter a date in the format YYYY-MM-DD: ")
date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d")

day_name = date_object.strftime("%A")
print("The day of the week is", day_name)



date_input = input("Enter a date in the format YYYY-MM-DD: CCCC ")
year, month, day = map(int, date_input.split("-"))

day_name = calendar.day_name[calendar.weekday(year, month, day)]
print("The day of the week isCCCC ", day_name)



