a = int(input())
b = int(input())
n = int(input())
lst_cdy = n * 3
a_lst_cdy = a - lst_cdy
b_lst_cdy = b - lst_cdy
if a_lst_cdy <= 0 and b_lst_cdy <= 0:
    print(0)
elif b <= lst_cdy:
    print(a_lst_cdy)
elif a <= lst_cdy:
    print(b_lst_cdy)
else:
    diff = abs(a_lst_cdy - b_lst_cdy)
    print(diff)