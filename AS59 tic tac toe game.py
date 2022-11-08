ttt = [['', '', ''], ['', '', ''], ['', '', '']]
print("The following is the code to define each box of the game:")
print("00 01 02\n"
      "10 11 12\n"
      "20 21 22")

user_x_win = False
user_y_win = False
game = False

def seq(num1, num2, num3):
    global user_x_win, user_y_win
    if num1 == 'x' and num2 == 'x' and num3 == 'x':
        user_x_win = True
        return True
    elif num1 == 'o' and num2 == 'o' and num3 == 'o':
        user_y_win = True
        return True
    return False

while True:
    print(ttt[0])
    print(ttt[1])
    print(ttt[2])
    count = 0
    x = input("Player 1:")
    numbers = list(x)
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    if ttt[numbers[0]][numbers[1]] != '':
        print("That cell is already occupied")
        continue
    ttt[numbers[0]][numbers[1]] = 'x'
    print(ttt[0])
    print(ttt[1])
    print(ttt[2])
    o = input("Player 2:")
    numbers_o = list(o)
    numbers_o[0] = int(numbers_o[0])
    numbers_o[1] = int(numbers_o[1])
    while ttt[numbers_o[0]][numbers_o[1]] != '':
        print("That cell is already occupied")
        o = input("Player 2:")
        numbers_o = list(o)
    ttt[numbers_o[0]][numbers_o[1]] = 'o'

    for lists in ttt:
        for elems in lists:
            if elems == '':
                count += 1
    if count == 0:
        break
    if seq(ttt[0][0], ttt[0][1], ttt[0][2]) or seq(ttt[1][0], ttt[1][1], ttt[1][2]) or seq(ttt[2][0], ttt[2][1], ttt[2][2]):
        game = True
        break
    if seq(ttt[0][0], ttt[1][0], ttt[2][0]) or seq(ttt[0][1], ttt[1][1], ttt[2][1]) or seq(ttt[0][2], ttt[1][2], ttt[2][2]):
        game = True
        break
    if seq(ttt[0][0], ttt[1][1], ttt[2][2]) or seq(ttt[0][2], ttt[1][1], ttt[2][0]):
        game = True
        break

if user_x_win:
    print("First player (playing x) won")
else:
    print("Second player (playing o) won")
