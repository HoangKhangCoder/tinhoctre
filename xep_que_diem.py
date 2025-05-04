import math
n = int(input())
index =  int(math.sqrt(n * 2 // 3))

while index * (index + 1) <= n * 2 // 3:
    index += 1

print(index - 1)