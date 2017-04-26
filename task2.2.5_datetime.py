import datetime

date = [int(t) for t in input().split()]
days = int(input())

date_obj = datetime.date(date[0], date[1], date[2])
date_obj += datetime.timedelta(days)
print(date_obj.year, date_obj.month, date_obj.day)



