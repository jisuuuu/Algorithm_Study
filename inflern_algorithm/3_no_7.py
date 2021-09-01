#사과나무(다이아몬드)
import sys
# sys.stdin = open("input.txt", "rt")
# n = 5 -> 1, 3, 5, 3, 1
# n = 3 -> 1, 3, 1
# n = 7 -> 1, 3, 5, 7, 5, 3, 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = 0

s = e = n // 2

for i in range(n):
    for j in range(s, e + 1):
        result += matrix[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(result)