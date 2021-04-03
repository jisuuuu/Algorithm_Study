#직사각형 네개의 합집합의 면적 구하기
import sys
matrix = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(4):
    l_x, l_y, r_x, r_y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            if matrix[j][i] == 0:
                matrix[j][i] = 1
                cnt += 1
print(cnt)