from datetime import datetime

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'

daf = '%d.%m.%Y'

def is_available_date(booked_dates,date_for_booking): #1 аргумент список строковых дат, недоступных для бронирования. 2 арг одиночная строковая дата или период (две даты через дефис), на который гость желает забронировать номер
  list_data_busy = []
  free = []
  daf = '%d.%m.%Y'
  if isinstance(booked_dates,list):
    for date in booked_dates:
      if '-' in date:
        a, b =  date.split('-')
        date_1 = datetime.strptime(a,daf)
        date_2 = datetime.strptime(b,daf)
        for i in range(int(date_1.timestamp()),int(date_2.timestamp())+86400,86400): #получаем период дат
          list_data_busy.append(datetime.fromtimestamp(i))  

      else:
        list_data_busy.append(datetime.strptime(date,daf)) 
  else:
    list_data_busy.append(datetime.strptime(booked_dates,daf))

  if isinstance(date_for_booking,list):
    for date in date_for_booking:
      if '-' in date:
        a, b =  date.split('-')
        date_1 = datetime.strptime(a,daf)
        date_2 = datetime.strptime(b,daf)
        for i in range(int(date_1.timestamp()),int(date_2.timestamp())+86400,86400):
          free_date = datetime.fromtimestamp(i)  
          if free_date in list_data_busy:
            flag = False
            break
          else:
            flag = True
      else:
        free_date = datetime.strptime(date,daf)
        if free_date in list_data_busy:
          flag = False
          break
        else:
          flag = True
  else:
    if '-' in date_for_booking:
      a, b =  date_for_booking.split('-')
      date_1 = datetime.strptime(a,daf)
      date_2 = datetime.strptime(b,daf)
      for i in range(int(date_1.timestamp()),int(date_2.timestamp())+86400,86400):
        free_date = datetime.fromtimestamp(i)
        #free.append(free_date)  
        if free_date in list_data_busy:
          flag = False
          break
        else:
          flag = True    
    else:  
      free_date = datetime.strptime(date_for_booking,daf)
      if free_date in list_data_busy:
        flag = False
      else:
        flag = True 
  
  if flag:
    return True
  else:
    return False
    

print(is_available_date(dates, some_date))