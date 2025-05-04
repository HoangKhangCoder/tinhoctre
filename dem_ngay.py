x = int(input())
y = int(input())
if y < 10**6:
    days = 0
    for year in range(x, y + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days += 366
        else:
            days += 365
else:
    years = list(range(x, y + 1))
    days = sum(366 for year in years if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0) + sum(365 for year in years if  year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
    days += sum(365 for year in years if  year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
print(days)