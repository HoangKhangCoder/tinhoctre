# a = int(input())
# n = int(input())
# result = 0
# nums = a
# k = a // 2
# for i in range(n):
#     result += nums % 10
#     if i % 2 == 0:
#         nums -= k
#     else:
#         nums += a
# print(result)
# ---------------------
nums_cycle = []
a = int(input())
n = int(input())
result = 0
nums = a
k = a // 2
for i in range(20):
    nums_cycle.append(nums % 10)
    if i % 2 == 0:
        nums -= k
    else:
        nums += a
result += sum(nums_cycle) * (n // 20)
result += sum(nums_cycle[:n%20])
print(result)