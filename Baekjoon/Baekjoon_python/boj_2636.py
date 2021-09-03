#치즈
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    check = [[False for _ in range(M)] for _ in range(N)]
    check[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not check[nx][ny]:
                    if matrix[nx][ny] >= 1:
                        matrix[nx][ny] += 1
                    else:
                        q.append((nx, ny))
                        check[nx][ny] = True


def melt():
    global piece
    melted = False
    cnt = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] >= 2:
                matrix[i][j] = 0
                melted = True
                cnt += 1
    if cnt:
        piece = cnt
    return melted


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

answer = 0
piece = 0

while True:
    bfs()

    if melt():
        answer += 1
    else:
        break

print(answer)
print(piece)