#마법사 상어와 토네이도

#모래 계산하는 함수
def solve(time, dx, dy, direction):
    global answer, s_x, s_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        s_x += dx
        s_y += dy
        if s_y < 0: #범위 밖에면 stop
            break

        # out_sand 구하기
        total = 0
        for x, y, z in direction:
            nx = s_x + x
            ny = s_y + y

            if z == 0:
                new_sand = sand[s_x][s_y] - total
            else:
                new_sand = int(sand[s_x][s_y] * z)
                total += new_sand

            if 0 <= nx < n and 0 <= ny < n:
                sand[nx][ny] += new_sand
            else:
                answer += new_sand



import sys
n = int(sys.stdin.readline().rstrip())
sand = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

s_x, s_y = n // 2, n // 2
answer = 0

for i in range(1, n + 1):
    if i % 2:
        solve(i, 0, -1, left)
        solve(i, 1, 0, down)
    else:
        solve(i, 0, 1, right)
        solve(i, -1, 0, up)
print(answer)