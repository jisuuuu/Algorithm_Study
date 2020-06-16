#탈출
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    check[x][y] = 1


def water():
    pass


M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(M)]
check = [[0 for _ in range(M)]for _ in range(N)]
q = deque()
wq = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            x, y = i, j
            matrix[i][j] = '.'

        elif matrix[i][j] == '*':
            wq.append([i, j])

bfs(x, y)