from datetime import datetime,time,date,timedelta



dates= datetime(year=1998,month=8,day=7,hour=12,minute=45)
print(type(dates))
print(dates.hour+dates.minute)
print(type(dates.hour+dates.minute))
b = timedelta(hours=9)

print(b.seconds//60)