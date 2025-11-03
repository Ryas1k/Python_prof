from datetime import datetime,time,date,timedelta

day = ['день', "дня", "дней"]
hour = ['час', 'часа', 'часов']
minute = ['минута', 'минуты', 'минут']
pattern='%d.%m.%Y %H:%M'

def choose_plural(amount, declensions):
  last_amount =  amount % 10
  if 11 <= amount % 100 < 20:
    return f"{amount} {declensions[2]}"
# Если последняя цифра 1, используем первую форму ('один').
  if last_amount == 1:
      return f"{amount} {declensions[0]}"
  # Если последняя цифра 2, 3 или 4, используем вторую форму ('два').
  if last_amount in [2, 3, 4]:
      return f"{amount} {declensions[1]}"
  # Во всех остальных случаях (0, 5, 6, 7, 8, 9) используем третью форму ('пять').
  return f"{amount} {declensions[2]}"

start_kyrs = datetime.strptime(input(),pattern)
exit_kyrs = datetime(2022,11,8,12)
if start_kyrs < exit_kyrs:
    finish = exit_kyrs - start_kyrs
    lim = [choose_plural(finish.days, day), choose_plural(finish.seconds // 3600,         hour),choose_plural((finish.seconds // 60) % 60, minute)]
    lim1 = ' и '.join([i for i in lim if int(i.split()[0])!=0][:2])
    print(f'До выхода курса осталось: {lim1}')
else:
    print('Курс уже вышел!')