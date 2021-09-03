#로봇 청소기
import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 0 북, 1 동, 2 남, 3 서


def clean(x, y, d):
    global answer

    if board[x][y] == 0:
        board[x][y] = 2
        answer += 1
    #1. 현재 위치를 청소한다

    for _ in range(4):
        nd = (d + 3) % 4 #왼쪽 방향
        nx = x + dx[nd]
        ny = y + dy[nd]

        if board[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        #2-a. 왼쪽방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸 전진하고 1번부터 진행
        d = nd
        #2-b. 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하고 다시 반복
    #2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색한다.

    #2-c. 네 방향 모두 청소 이미 되어있거나 벽인 경우 바라보는 방향에서 후진하고 2번
    nd = (d + 2) % 4 #후진한 방향
    nx = x + dx[nd]
    ny = y + dy[nd]

    if board[nx][ny] == 1:
        return #2-d. 후진도 할 수 없는 경우 작동을 멈춤
    clean(nx, ny, d) #바라보는 방향은 유지하기 때문에


n, m = map(int, sys.stdin.readline().rstrip().split())
x, y, d = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
answer = 0
clean(x, y, d)
print(answer)