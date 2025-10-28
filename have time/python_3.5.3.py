from datetime import datetime,time,date,timedelta

schedule = (
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=10), timedelta(hours=18)),
    (timedelta(hours=10), timedelta(hours=18))
)

pattern='%d.%m.%Y %H:%M'
def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60   

dates= datetime.strptime(input(),pattern)
index_1 = dates.weekday()
index_2 = dates.weekday() +1

start = schedule[index_1][0]
end = schedule[index_1][1]
times = timedelta(hours=dates.hour,minutes=dates.minute,seconds=dates.second)

if start <= times < end:
    difference_times = end - times 
    #print('Время разность конца и текущего:',difference_times)
    hours,minutes = hours_minutes(difference_times)
    print(hours*60+minutes)
else:
    print('Магазин не работает')
