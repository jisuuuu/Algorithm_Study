#인구 이동
import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, l, r = map(int, sys.stdin.readline().rstrip().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
country = []
day = 0

for _ in range(n):
    country.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    union = [(i, j)]

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
                    union.append((nx, ny))

    return union

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)

                if len(union) > 1:
                    flag = True
                    total = sum(country[x][y] for x, y in union) // len(union)

                    for x, y in union:
                        country[x][y] = total
    if not flag:
        break
    day += 1

print(day)