#블록 이동하기
#개개개개개 어렵당 다른 분 코드
from collections import deque

# 로봇의 위치에서 이동할 수 있는 좌표 판단 기준 (1, 0) 우 (-1, 0) 좌 (0, 1) 상 (0, -1) 하
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
c = []

def bfs(r, b, m, n):
    q.append(r)
    c.append(r)
    cnt = 0
    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()
            # 로봇이 가로로 [n - 1, n], [n, n] 세로로 [n, n - 1], [n, n] 에 있다면 멈춤
            if x == [[m - 1, n - 2], [m - 1, n - 1]] or x == [[m - 2, n - 1], [m - 1, n - 1]]:
                return cnt

            # dx, dy 좌표 갯수 만큼 전진 가능 여부 확인
            for i in range(4):
                temp = []
                flag = 0

                # 로봇의 위치 전부 확인
                for j in range(2):
                    nx = x[j][0] + dx[i]
                    ny = x[j][1] + dy[i]

                    # 이동 좌표가 n, m 미만이고 해당 좌표가 비어있으면 temp에 저장
                    if 0 <= nx < m and 0 <= ny < n and b[nx][ny] == 0:
                        temp.append([nx, ny])
                    else:
                        flag = 1 # 이동 가능한 범위를 체크하기 위함 하나라도 flag 되면 이동이 안되는 것
                        break

                # 전부 확인했는데 flag가 없다면 실제로 이동!
                if not flag:
                    if x[0][0] == x[1][0]: #로봇이 가로로 있고 세로로 이동이 가능할 때
                        if i == 0 or i == 1:
                            turn(x, i, '|')

                    elif x[0][1] == x[1][1]: #로봇이 세로로 있고 가로로 이동이 가능할 때
                        if i == 2 or i == 3:
                            turn(x, i, '-')

                    #로봇이 원래 있는 방향으로 직진하는 경우
                    temp.sort() #정렬해서 중복되는 케이스 배재
                    if temp not in c: # 거처간 리스트 c에도 없다면 넣어줌
                        q.append(temp)
                        c.append(temp)
            qlen -= 1
        cnt += 1

def turn(x, i, mode):
    if mode == '|':
        for j in range(2):
            nx = x[j]
            ny = [x[j][0] + dx[i], x[j][1]]
            temp = [nx, ny]
            temp.sort()
            if temp not in c:
                q.append(temp)
                c.append(temp)

    elif mode == '-':
        for j in range(2):
            nx = [x[j][0], x[j][1] + dy[i]]
            ny = x[j]
            temp = [nx, ny]
            temp.sort()
            if temp not in c:
                q.append(temp)
                c.append(temp)

def solution(board):
    m, n = len(board), len(board[0])
    robot = [[0, 0], [0, 1]]
    return(bfs(robot, board, m, n))