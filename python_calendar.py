import calendar
from datetime import date


def get_all_mondays(year):
    l_date = []
    for month in range(1, 13):
        days_month = calendar.monthrange(year, month)[1]
        for day in range(1, days_month + 1):
            dt = calendar.weekday(year, month, day)
            if dt == 0:
                l_date.append(date(year, month, day))
    return l_date

print(get_all_mondays(2021))