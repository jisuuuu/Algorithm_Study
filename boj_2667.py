# 단지번호붙이기
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def dfs(x, y, matrix, N):
    global cnt
    matrix[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if matrix[nx][ny] == 1:
            dfs(nx, ny, matrix, N)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    answer = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                dfs(i, j, matrix, N)
                answer.append(cnt)
                cnt = 0

    print(len(answer))
    answer.sort()
    for a in answer:
        print(a)