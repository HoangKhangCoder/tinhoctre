num = input()
letters = list(num)
right_num = 0
for number in range(10,0,-1):
    for index in range(len(letters)):
        if letters[index] == number:
            letters[index] == number