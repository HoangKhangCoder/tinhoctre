len_num = int(input())
num = input()
k = int(input())
nums = list(num)
i = 0
if int(num) % 2 != 0:
    nums[-1] = '0'
    k -= 1
while k > 0 and i < len(nums):
    if i == 0:
        if int(nums[i]) != 1:
            nums[i] = '1'
            k -= 1
    else:
        if int(nums[i]) != 0:
            nums[i] = '0'
            k -= 1
    i += 1
print(''.join(nums))