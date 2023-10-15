# Dates

from datetime import datetime

now = datetime.now()
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


year_2023 = datetime(2023,10,13)

print_date(year_2023)





