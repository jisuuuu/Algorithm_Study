#마법사 상어와 비바라기
import sys
from collections import deque

#명령 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
#물복사버그 마법
sx = [-1, -1, 1, 1]
sy = [-1, 1, -1, 1]
n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
clouds = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for _ in range(m):
    d, s = map(int, sys.stdin.readline().rstrip().split())
    #한 바퀴 돌면 리셋
    visited = [[False for _ in range(n)] for _ in range(n)]
    d -= 1
    c_len = len(clouds)

    # 모든 구름 d방향으로 s칸 이동한다
    while c_len:
        cx, cy = clouds.popleft()
        nx = (n + cx + dx[d] * s) % n
        ny = (n + cy + dy[d] * s) % n

        clouds.append((nx, ny))
        c_len -= 1

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다, 구름 표시
    for cx, cy in clouds:
        if not visited[cx][cy]:
            matrix[cx][cy] += 1
            visited[cx][cy] = True

    #물복사버그 마법
    for cx, cy in clouds:
        cnt = 0
        for i in range(4):
            mx = cx + sx[i]
            my = cy + sy[i]

            if 0 <= mx < n and 0 <= my < n:
                if matrix[mx][my] > 0:
                    cnt += 1
        matrix[cx][cy] += cnt

    #구름 모두 사라진다
    clouds = deque()

    #구름이였던 것 빼고 구름 재설정
    for i in range(n):
        for j in range(n):
            if matrix[i][j] >= 2 and visited[i][j] == False:
                clouds.append((i, j))
                matrix[i][j] -= 2

answer = 0
for m in matrix:
    answer += sum(m)
print(answer)