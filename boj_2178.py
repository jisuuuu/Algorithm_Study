# 미로탐색
from collections import deque
import sys


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and matrix[nx][ny] == 1:
                q.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1


n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

bfs(0, 0)
print(matrix[n - 1][m - 1])
