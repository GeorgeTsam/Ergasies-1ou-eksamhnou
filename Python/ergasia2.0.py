import random

square = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
steps = []
for i in range(1, 101):
    x = 0
    end = True
    while end:
        x += 1
        cap = random.randint(1, 3)
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if cap == 1:
            if square[row][col] == 0:
                square[row][col] = cap
        elif cap == 2:
            if square[row][col] == 0 or square[row][col] == 1:
                square[row][col] = cap
        else:
            if square[row][col] == 0 or square[row][col] == 2 or square[row][col] == 1:
                square[row][col] = cap

    if square[0][0] == square[0][1] and square[0][1] == square[0][2] and square[0][0] != 0:
        end = False
    elif square[1][0] == square[1][1] and square[1][1] == square[1][2] and square[1][0] != 0:
        end = False
    elif square[2][0] == square[2][1] and square[2][1] == square[2][2] and square[2][0] != 0:
        end = False
    elif square[0][0] == square[1][0] and square[1][0] == square[2][0] and square[0][0] != 0:
        end = False
    elif square[0][1] == square[1][1] and square[1][1] == square[2][1] and square[0][1] != 0:
        end = False
    elif square[0][2] == square[1][2] and square[1][2] == square[2][2] and square[0][2] != 0:
        end = False
    elif square[0][0] == square[1][1] and square[1][1] == square[2][2] and square[0][0] != 0:
        end = False
    elif square[2][0] == square[1][1] and square[1][1] == square[0][2] and square[0][0] != 0:
        end = False

    steps[i] = x
total = 0
for i in range(1, 101):
    total = total + steps[i]
average = total/100
print(average)
