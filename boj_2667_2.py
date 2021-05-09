#단지번호 붙이기 bfs
import sys
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))

    matrix[i][j] = '0'
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and matrix[nx][ny] == '1':
                matrix[nx][ny] = '0'
                cnt += 1
                q.append((nx, ny))

    return cnt


n = int(sys.stdin.readline().rstrip())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            answer.append(bfs(i, j))
print(len(answer))
answer.sort()
for a in answer:
    print(a)