#상어 초등학교
import sys
from collections import defaultdict

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(sys.stdin.readline().rstrip())
seats = [[0 for _ in range(n)] for _ in range(n)]
students = defaultdict(list)

for _ in range(n * n):
    new = list(map(int, sys.stdin.readline().rstrip().split()))
    students[new[0]] = new[1:]

    max_empty, max_like = -1, -1 #음수여야 통과... 최대값이 0인 경우가 있나봄..
    max_i, max_j = 0, 0

    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                empty_cnt = 0
                like_cnt = 0

                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j

                    if 0 <= nx < n and 0 <= ny < n:
                        if seats[nx][ny] in new:
                            like_cnt += 1
                        if seats[nx][ny] == 0:
                            empty_cnt += 1

                if max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                    max_i = i
                    max_j = j
                    max_like = like_cnt
                    max_empty = empty_cnt

    seats[max_i][max_j] = new[0]

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0

        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j

            if 0 <= nx < n and 0 <= ny < n:
                if seats[nx][ny] in students[seats[i][j]]:
                    cnt += 1

        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)