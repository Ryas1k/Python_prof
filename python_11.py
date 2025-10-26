from datetime import datetime, timedelta, date

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']


def fill_up_missing_dates(dates):
    form = '%d.%m.%Y'
    new_dates = [datetime.strptime(d,form) for d in dates]
    st, end = min(new_dates), max(new_dates)
    days = (end-st).days
    return [(st+timedelta(days=d)).strftime(form) for d in range(days+1)]
    

print(fill_up_missing_dates(dates))
