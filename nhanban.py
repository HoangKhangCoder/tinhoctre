a = int(input())
l = int(input())
r = int(input())
a_reverse_list = list(map(int, list(str(a)[::-1])))
a_list = list(map(int, list(str(a))))
sum_a = sum(a_list)
len_a = len(a_list)
a_hst_clted = a
if (l - r + 1) % len_a == 0:
    print((l - r + 1) // len_a * sum_a)
else:
    if l // len_a == 0:
        result = sum(a_list[l - 1:])
    else:
        result = sum(a_reverse_list[l - 1:])
    a_hst_clted -= len(a_list[l - 1:])
    result += a_hst_clted // len_a * sum_a
    a_hst_clted -= a_hst_clted // len_a * len_a
    if r // len_a == 0:
        result = sum(a_list[l - 1:])
    else:
        result = sum(a_reverse_list[l - 1:])
print(result)