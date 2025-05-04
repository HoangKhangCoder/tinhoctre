# input
a = int(input())
t = int(input())
k = int(input())

# define to count k
def count_k(start, end):
    value_return = 0
    for minute in range(start, end + 1):
        if minute // 10 == k:
            value_return += 1
        if minute % 10 == k:
            value_return += 1
    return value_return
# calculate number k in an hour
numkin1hour = count_k(0, 59)
remain = t - (59 - a + 1)
# check a + t in range 60 minutes
if a + t <= 60:
    result = count_k(a, a + t)
elif (a + t) % 60 == 0:
    result = numkin1hour * (a + remain) // 60
else:
    # part 1: first remain
    result = count_k(a, 59)
    # part 2: count the number k in an hour
    result += remain // 60 * numkin1hour
    # part 3: result plus the last remain
    result += count_k(0, remain % 60)
print(result)