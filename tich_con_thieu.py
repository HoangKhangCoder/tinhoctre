# n, m = map(int, input().split())
# a = input()
# re_a = a.replace(' ', '')
# nums = list(re_a)
# mul = 1
# MOD = 10 ** 9 + 7
# #   for i in range(1, m + 1):
# #       if str(i) not in nums:
# #           mul *= i % MOD
# #           mul %= MOD
# #    print(mul)
# full_nums = list(range(1, m + 1))
# missing_nums = list(set(full_nums) - set(map(int, nums)))
# for item in missing_nums:
#     mul *= item
#     mul %= MOD
# print("nums:", nums)
# print("full_nums:", full_nums)
# print("missing_nums:", missing_nums)
# print("multiply:", mul)


#-------------------------------------
n_m_input = input()
# print(n_m_input)
n_m_split = n_m_input.split()
# print(n_m_split)

n, m = list(map(int, n_m_split))
# print(n, m)

nums = list(map(int, input().split()))
mul = 1
MOD = 10 ** 9 + 7

full_nums = list(range(1, m + 1))
missing_nums = list(set(full_nums) - set(nums))
if missing_nums:
    for item in missing_nums:
        mul = ((mul % MOD) * (item % MOD)) % MOD
else:
    mul = 0
print(mul)