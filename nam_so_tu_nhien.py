nums1 = 0
nums2 = 0
for i in range(5):
    a = int(input())
    if a == 1:
        nums1 += 1
    else:
        nums2 += 1
if nums1 > nums2:
    print(1)
else:
    print(2)