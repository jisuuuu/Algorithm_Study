#전투

import sys
from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))

    c = soliders[y][x]
    soliders[y][x] = 1
    cnt = 0

    while q:
        y, x = q.popleft()

        cnt += 1

        for i in range(4):
            d_y, d_x = y + dy[i], x + dx[i]

            if (0 <= d_y < m) and (0 <= d_x < n) and soliders[d_y][d_x] == c:
                q.append((d_y, d_x))
                soliders[d_y][d_x] = 1

    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
soliders = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

our = []
enemy = []

for i in range(m):
    for j in range(n):
        if soliders[i][j] == 'W':
            our.append(bfs(i, j) ** 2)
        elif soliders[i][j] == 'B':
            enemy.append(bfs(i, j) ** 2)

print(f'{sum(our)} {sum(enemy)}')