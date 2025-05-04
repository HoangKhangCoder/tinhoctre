LOOK_UP = {
    'T': 4,
    'I': 1,
    'N': 1,
    'H': 2,
    'O': 1,
    'C': 1,
    'R': 1,
    'E': 1,
}
repeat = int(input())
letter = input()
spc_clr = 1
num_repeat = repeat // 4
remain = repeat % 4 * 9
result = LOOK_UP[letter] * num_repeat
for i in range(1, remain + 1):
    if  i == 1 or (spc_clr == 1 and i % 4 == 0) or (i - 1) % 4 == 0: # Check color
        if 'TINHOCTRE'[(i - 1) % 9] == letter: # Check letter
            result += 1
    if i % 4 == 0:
        spc_clr += 1
        if spc_clr > 3:
            spc_clr = 1
print(result)