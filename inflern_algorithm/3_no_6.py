#격자판 최대합
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_num = -sys.maxsize

#행과 열의 합
for i in range(n):
    sum1, sum2 = 0, 0
    for j in range(n):
        sum1 += matrix[i][j]
        sum2 += matrix[j][i]

    if max_num < sum1:
        max_num = sum1
    if max_num < sum2:
        max_num = sum2

#대각선의 합
sum1, sum2 = 0, 0
for i in range(n):
    sum1 += matrix[i][i]
    sum2 += matrix[n - i - 1][n - i - 1]

if max_num < sum1:
    max_num = sum1
if max_num < sum2:
    max_num = sum2

print(max_num)