#최댓값
import sys
board = []

for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

x, y = 0, 0
max_num = -1

for i in range(9):
    for j in range(9):
        if board[i][j] > max_num:
            max_num = board[i][j]
            x = i + 1
            y = j + 1
print(max_num)
print(x, y)