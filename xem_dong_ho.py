n = int(input())
time = [0, 0, 0, 0]
result = 0
great_time = []
for sum_minute in range(1, n + 1):
    hour = sum_minute // 60
    minute = sum_minute % 60
    time = [hour // 10, hour % 10, minute // 10, minute % 10]
    great_time.append(time)
    if time[0] < time[1] and time[1] < time[2] and time[2] < time[3]:
        result += 1
print(result)