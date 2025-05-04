a = int(input())
b = int(input())
c = int(input())
d = int(input())
abcd = [a, b, c, d]
pairs =[]
for item in range(len(abcd)):
    for another_item in range(len(abcd)):
        pairs.append(abcd[item] * 10 + abcd[another_item])

print(set(pairs))
print(sum(1 for item in set(pairs) if item % 2 == 0 and len(str(item)) == 2))