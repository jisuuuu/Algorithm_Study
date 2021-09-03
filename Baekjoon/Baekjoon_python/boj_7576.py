#토마토 bfs
import sys
from collections import deque


def bfs(n, m):
    cnt = -1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if (0 <= nx < n) and (0 <= ny < m) and matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])

    for mat in matrix:
        if 0 in mat:
            return -1
    return cnt


m, n = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append((i, j))
print(bfs(n, m))