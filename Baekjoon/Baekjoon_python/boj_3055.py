#탈출
#물흐르기 -> 고슴도치 건너기
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    check[x][y] = 1

    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N:
                    if matrix[nx][ny] == '.' and check[nx][ny] == 0:
                        check[nx][ny] = check[x][y] + 1
                        q.append([nx, ny])

                    elif matrix[nx][ny] == 'D':
                        print(check[x][y])
                        return
            qlen -= 1
        water()
    print('KAKTUS')
    return


def water():
    wqlen = len(wq)

    while wqlen:
        x, y = wq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if matrix[nx][ny] == '.':
                    matrix[nx][ny] = '*'
                    wq.append([nx, ny])

        wqlen -= 1

M, N = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(M)]
check = [[0 for _ in range(N)] for _ in range(M)] #시간계산 DP
q = deque()
wq = deque()

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'S':
            x, y = i, j #출발위치 저장
            matrix[i][j] = '.'

        elif matrix[i][j] == '*':
            wq.append([i, j]) #물 queue 저장

water()
bfs(x, y)