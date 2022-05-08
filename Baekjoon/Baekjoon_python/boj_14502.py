#연구소
import sys
import copy
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, sys.stdin.readline().rstrip().split())
lab = list()
result = 0

for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bfs():
    global result
    q = deque()
    l = copy.deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if l[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if l[nx][ny] == 0:
                    l[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0
    for i in l:
        cnt += i.count(0)
    result = max(result, cnt)


def wall(x):
    if x == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(x + 1)
                lab[i][j] = 0
wall(0)
print(result)