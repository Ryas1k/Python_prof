from datetime import datetime,timedelta

forma = '%H:%M'
time_start = datetime.strptime(input(),forma)
time_end = datetime.strptime(input(),forma)

while time_start <= time_end:
 time_end_yrok = time_start+timedelta(seconds=45*60) #время плюс 45 мин   
 if time_end_yrok <= time_end:
    print(time_start.strftime(forma), '-' ,time_end_yrok.strftime(forma))
    time_start = time_end_yrok+timedelta(seconds=10*60)
 else:
    break
