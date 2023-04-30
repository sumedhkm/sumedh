import datetime as dt

current_date=dt.date.today()
print("current date:",current_date)

new=dt.date(2021,10,25)
print(new)
print("year:",new.year)
print("month:",new.month)
print("day:",new.day)
print("-----------------------")

a=dt.time(10,45,5,555505)
print(a)
print("hour:",a.hour)
print("minute:",a.minute)
print("second:",a.second)
print("microsecond:",a.microsecond)
print("-----------------------")

current_time=dt.datetime.now()
print("current time:",current_time)
print("-----------------------")
new=dt.datetime(2022,12,2,3,4,5)
print(new)
print(new.date())
print(new.time())

print("-----------------------")
current=dt.datetime(2023,5,1)
new_year=dt.datetime(2024,3,2)
difference=current-new_year
print(difference)
print("-----------------------")
current=dt.datetime.now()
print(current)
s=current.strftime("%A %B %D %Y")
print(s)



