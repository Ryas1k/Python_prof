import calendar
from datetime import date

def get_all_mondays(year):
  l_date = []        
  for month in range(1,13):
      if calendar.monthcalendar(year, month)[0][3] == 0: # Условие что четверг существует в первой недели
        free_thursday = calendar.monthcalendar(year, month)[3][3]  # Определяем четверг какой день если есть в первой недели
      else:
        free_thursday = calendar.monthcalendar(year, month)[2][3]  # Определяем четверг какой день
      l_date.append(date(year,month,free_thursday))         
  return [i.strftime('%d.%m.%Y') for i in l_date]


print(*get_all_mondays(2021),sep='\n')