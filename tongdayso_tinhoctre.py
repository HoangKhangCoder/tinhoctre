k = int(input())
num = int(input())
safe_num = num // k
result = safe_num * (safe_num + 1) / 2 * k
result += (num - safe_num * k) * (safe_num + 1)
print(result)