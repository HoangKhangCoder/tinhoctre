n = int(input())
k = int(input())
if n * (n + 1) / 2 <= k:
    result = 0
else:
    result = (k // (n + 1)) * 2
    if (result / 2) * (n + 1) <= k:
        if (result / 2) + 1 + (result / 2) * (n + 1) > k:
            result += 1
        else:
            result += 2
print(result)