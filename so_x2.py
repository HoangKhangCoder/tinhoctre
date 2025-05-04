# n  = int(input())
# result = 0
# last_2_num = 1
# last_1_num = 3
# for num in range(n):
#     if num == 0:
#         result += 1
#     elif num == 1:
#         result += 3
#     else:
#         result += last_2_num * 2 % 100
#         last_2_num, last_1_num = last_1_num, last_2_num * 2 % 100
# print(result)
# -----------------------------------------------------
# Tính chu kỳ
# cycle_nums = []
# i = 0
# while 56 not in cycle_nums:
#     if i == 0:
#         cycle_nums.append(1)
#     elif i == 1:
#         cycle_nums.append(3)
#     else:
#         cycle_nums.append((cycle_nums[i - 2] * 2) % 100)
#     i += 1
# print(len(cycle_nums) - 4)
# print(cycle_nums)
# print(sum(cycle_nums[4:]))
# 13
# [1, 3, 2, 6, 4, 12, 8, 24, 16, 48, 32, 96, 64, 92, 28, 84, 56]
# 570 sum
# ----------------------------------------------------------
cycle_nums = [4, 12, 8, 24, 16, 48, 32, 96, 64, 92, 28, 84, 56, 68, 12, 36, 24, 72, 48, 44, 96,
    88, 92, 76, 84, 52, 68, 4, 36, 8, 72, 16, 44, 32, 88, 64, 76, 28, 52, 56]
sum_cycle_num = 2000

n  = int(input())
result = 12
look_up_4 = [1, 3, 4, 6]
if n < 4:
    print(sum(look_up_4[:n]))
else:
    result += ((n - 4) // 40) * sum_cycle_num
    if (n - 4) % 40 > 0:
        result += sum(cycle_nums[:(n - 4) % 40])
    print(result)