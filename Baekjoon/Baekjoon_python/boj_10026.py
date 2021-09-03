#적록색약
import sys
sys.setrecursionlimit(100000) #파이썬 가능 재귀 깊이 1000인데 늘려주는 장치

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
normal_cnt = 0
abnormal_cnt = 0


def normal_dfs(x, y, c, visited, matrix):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if matrix[nx][ny] == c and visited[nx][ny] == 0:
            normal_dfs(nx, ny, c, visited, matrix)


def abnormal_dfs(x, y, c, ab_visited, matrix):
    ab_visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if c == 'R' or c == 'G':
            if (matrix[nx][ny] == 'R' or matrix[nx][ny] == 'G') and ab_visited[nx][ny] == 0:
                abnormal_dfs(nx, ny, c, ab_visited, matrix)

        elif matrix[nx][ny] == c and ab_visited[nx][ny] == 0:
            abnormal_dfs(nx, ny, c, ab_visited, matrix)


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ab_visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                normal_cnt += 1
                normal_dfs(i, j, matrix[i][j], visited, matrix)

            if ab_visited[i][j] == 0:
                if matrix[i][j] == 'G':
                    abnormal_cnt += 1
                    abnormal_dfs(i, j, 'R', ab_visited, matrix)
                else:
                    abnormal_cnt += 1
                    abnormal_dfs(i, j, matrix[i][j], ab_visited, matrix)
    print(f'{normal_cnt} {abnormal_cnt}')