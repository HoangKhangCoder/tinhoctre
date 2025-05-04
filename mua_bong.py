need = int(input())
money = 17 * (need // 10)
need %= 10
money += 9 * (need // 5)
need %= 5
money += 2 * need
print(money)