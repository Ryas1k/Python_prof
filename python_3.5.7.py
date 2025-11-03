from datetime import datetime,time,date,timedelta

birthday_people = []
d={}
pattern='%d.%m.%Y'
start_dates = datetime.strptime(input(),pattern)
for i in range(int(input())):
    name,dt_birth = input().rsplit(' ',1) 
    d[datetime.strptime(dt_birth,pattern)] = name
weeks = 7 
for i in range(1,weeks+1):
    start_dates = start_dates+timedelta(days=1) 
    for birth_date, name in d.items():
        if birth_date.replace(year=start_dates.year) == start_dates:
            birthday_people.append((birth_date, name))           
if birthday_people:
    p = max(birthday_people,key=lambda x: x[0])
    print(p[1])
else:
    print('Дни рождения не планируются')