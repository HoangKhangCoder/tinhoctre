nums = list(input())
k = int(input())
for i in range(len(nums)):
    nums[i] = str((int(nums[i]) + k) % 10)
print(''.join(nums))