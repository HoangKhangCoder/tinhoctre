# n = int(input())
# result = [num * (num + 1) // 2 for num in range(1, n + 1) if num * (num + 1) % 12 == 0]
# print('nums:',result)
# print('answer:', len(result))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# nums_cycle = []
# for i in range(1, 31):
#     if i*(i + 1) % 12 == 0:
#         nums_cycle.append((i, 0))
#     else:
#         nums_cycle.append(i)
# print(nums_cycle)
n = int(input())
result = 4 * (n // 12)
remain = n % 12
if remain >= 11:
    result += 3
elif remain >= 8:
    result += 2
elif remain >= 3:
    result += 1
print(result)